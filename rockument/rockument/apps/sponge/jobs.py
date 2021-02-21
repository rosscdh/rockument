import zipfile
from pathlib import Path
from django_rq import job
from .models import Revision
from .services import FileHandlerService, CommonSegmentService

import logging
logger = logging.getLogger(__name__)


@job
def process_upload(revision: Revision, **kwargs):
    service = FileHandlerService()
    # download file
    tmp_file_name = service.download(revision.data.get('tmp_file_name'))
    if not tmp_file_name.exists():
        raise Exception(f"{tmp_file_name} does not exist, cant unzip")

    # unzip file
    target_dir = Path(f"{str(tmp_file_name)}-unzip")
    if not target_dir.exists():
        target_dir.mkdir()

    with zipfile.ZipFile(tmp_file_name, 'r') as zip:
        zip.extractall(target_dir)
    # upload files
    segment_service = CommonSegmentService(target_dir.glob('**/*'))
    common_path = segment_service.process()
    for item in target_dir.glob(f"{common_path}**/*"):

        if item.is_file():
            # we only want files as dirs are virutal
            part_index = item.parts.index('public') + 1 # from the public folder onwards
            filename = '/'.join(item.parts[part_index:])
            target_file_name = str(revision.s3_base_path(filename))
            service.upload(local_file_path=str(item), file_name=target_file_name)
            print(f"uploaded {target_file_name}")
            logger.info(f"uploaded {target_file_name}", extra={'target_file_name': target_file_name, 'app': revision.app.slug, 'revision': revision.revision})
    # cleanup
    # if target_dir.exists():
    #     target_dir.rmdir()
    # if tmp_file_name.exists():
    #     tmp_file_name.unlink()
