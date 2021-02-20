from django.views import generic
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from rockument.apps.sponge.models import App, Revision

class RevisionDetailView(generic.DetailView):
  model = App
  query_pk_and_slug = True
  response_class = HttpResponseRedirect
  def render_to_response(self, context, **response_kwargs):
      target_revision = self.kwargs.get('revision', 'latest')

      if target_revision == 'latest':
        target_revision = self.object.revision_set.all().order_by('revision').first()
      else:
        target_revision = get_object_or_404(Revision, revision=target_revision)
      redirect_url = f"{settings.S3_PUBLIC_URL}{settings.AWS_S3_BUCKET_NAME}/{target_revision.s3_base_path()}/"
      
      return self.response_class(
          redirect_to=redirect_url
      )