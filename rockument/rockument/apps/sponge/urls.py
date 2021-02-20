from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rockument.apps.sponge import views


urlpatterns = [
    path('', csrf_exempt(views.UploadRevisionView.as_view()))
]
