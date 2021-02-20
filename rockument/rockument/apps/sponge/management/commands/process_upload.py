from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from rockument.apps.sponge.models import Revision
from rockument.apps.sponge.jobs import process_upload


class Command(BaseCommand):
    help = 'Process the revision id'

    def add_arguments(self, parser):
        parser.add_argument('-revision_id', '-r', nargs='+', type=int)

    def handle(self, *args, **options):
        for rev in Revision.objects.filter(pk__in=options['revision_id']):
            self.stdout.write(self.style.NOTICE(f"Processing {rev}"))
            process_upload.delay(revision=rev,
                                 is_async=settings.USE_ASYNC)

            self.stdout.write(self.style.SUCCESS(f"Processed {rev}"))