from django.contrib import admin

from .models import App, Revision

admin.site.register(App)
admin.site.register(Revision)