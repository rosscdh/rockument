from django.views import generic
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

from .jobs import process_upload
from .models import App, Revision
from .forms import UploadRevisionForm


class UploadRevisionView(generic.FormView):
    form_class = UploadRevisionForm

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        # import pdb;pdb.set_trace()
        if not form.is_valid():
            return self.form_invalid(form)

        slug = form.slug()
        tmp_file_name = form.upload_for_processing()
        app, is_new = App.objects.get_or_create(slug=slug, name=form.cleaned_data.get('app'))
        revision = Revision.objects.create(app=app,
                                           revision=form.cleaned_data.get('revision'),
                                           repo=form.cleaned_data.get('repo'),
                                           data=dict(tmp_file_name=tmp_file_name))
        # import pdb;pdb.set_trace()
        process_upload.delay(revision=revision,
                             is_async=settings.USE_ASYNC) # Enqueue function in "default" queue
        return HttpResponse('ok')