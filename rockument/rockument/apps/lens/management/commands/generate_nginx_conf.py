from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.template.loader import render_to_string


class Command(BaseCommand):
    help = 'Generate nginx config'

    # def add_arguments(self, parser):
    #     parser.add_argument('-revision_id', '-r', nargs='+', type=int)

    def handle(self, *args, **options):
        data = {
            'S3_BUCKET_URL': settings.S3_BUCKET_URL,
            'S3_PROXY_STATIC_SERVER_URL': settings.S3_PROXY_STATIC_SERVER_URL,
        }
        nginx_conf = render_to_string('lens/nginx.conf', data)
        print(nginx_conf)