from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/drq/', include('django_rq.urls')),
    path('admin/', admin.site.urls),
    path('', include("rockument.apps.default.urls")),
    path('u/', include("rockument.apps.sponge.urls")),
    path('v/', include("rockument.apps.lens.urls")),
]
if settings.DEBUG is True:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)