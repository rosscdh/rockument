from django.apps import AppConfig
from django.db.models.signals import pre_save
from .signals import ensure_slug


class SpongeConfig(AppConfig):
    name = 'rockument.apps.sponge'

    def ready(self):
        from .models import App
        pre_save.connect(ensure_slug,
                         sender=App,
                         dispatch_uid='app.pre_save.ensure_slug')