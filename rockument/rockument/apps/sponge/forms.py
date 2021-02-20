import boto3
from django import forms
from django.template.defaultfilters import slugify
from .services import FileHandlerService


class UploadRevisionForm(forms.Form):
    app         = forms.CharField()
    revision    = forms.CharField()
    repo        = forms.CharField()
    payload     = forms.FileField()

    def slug(self):
        return slugify(self.cleaned_data.get('app'))

    def tmp_file_name(self):
        payload = self.cleaned_data.get('payload')
        suffix = payload.content_type.split('/')[-1]
        file_name = f"tmp-{self.slug()}-{self.cleaned_data.get('revision')}.{suffix}"
        return file_name

    def upload_for_processing(self) -> str:
        payload = self.cleaned_data.get('payload')
        suffix = payload.content_type.split('/')[-1]
        service = FileHandlerService()
        service.upload(local_file_path=payload.temporary_file_path(), file_name=self.tmp_file_name())
        return self.tmp_file_name()
