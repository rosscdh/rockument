import boto3
from pathlib import Path
from django.conf import settings


class FileHandlerService:
    def __init__(self, *args, **kwargs):
        self.session = boto3.session.Session(aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                             aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    def client(self):
        return self.session.resource('s3', 
                                     endpoint_url=settings.S3_URL,
                                     config=boto3.session.Config(signature_version='s3v4'))

    def upload(self, local_file_path: Path, file_name: str):
        s3 = self.client()
        s3.meta.client.upload_file(local_file_path,
                                   settings.AWS_S3_BUCKET_NAME,
                                   file_name)

    def download(self, remote_file_name) -> Path:
        s3 = self.client()
        tmp_file_name = f"/tmp/{remote_file_name}"
        with open(tmp_file_name, 'wb') as f:
            s3.meta.client.download_fileobj(settings.AWS_S3_BUCKET_NAME,
                                            remote_file_name, f)
        return Path(tmp_file_name)