import boto3
from pathlib import Path
from ordered_set import OrderedSet
from django.conf import settings


class CommonSegmentService:
    """
    Service to find the common root folder in a set of files extracted to a location
    matrix is a glob matrix of Posix Path objects
    """
    forbidden_sys_junk = (
        '__MACOSX'
    )
    def __init__(self, matrix: list):
        matrix = [str(line).strip().split('/') for line in matrix if isinstance(line, Path)]
        for forbidden in self.forbidden_sys_junk:
            matrix = [i for i in matrix if forbidden not in str(i)]
        # import pdb;pdb.set_trace()
        self.matrix = matrix

    def process(self) -> str:
        common_segments = list(OrderedSet(self.matrix[0]).intersection(*self.matrix[1:]))
        if common_segments:
            return f"{common_segments[-1]}/"
        return ''


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