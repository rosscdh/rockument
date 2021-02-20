from pathlib import Path
from django.db import models

class App(models.Model):
    slug = models.SlugField(max_length=128, unique=True)
    name = models.CharField(max_length=256)
    data = models.JSONField(default=dict, blank=True, null=False)

    def __str__(self):
        return self.name


class Revision(models.Model):
    app = models.ForeignKey('sponge.App', on_delete=models.CASCADE)
    revision = models.CharField(max_length=64)
    repo = models.URLField(blank=True, null=True)
    data = models.JSONField(default=dict, blank=True, null=False)

    class Meta:
        unique_together = [['app', 'revision']]

    def __str__(self):
        return f"{self.app.slug}@{self.revision}"

    def s3_base_path(self, file_name: str=None) -> Path:
        base_path = Path(f"{self.app.slug}/{self.revision}")
        if file_name:
            return base_path / file_name
        return base_path