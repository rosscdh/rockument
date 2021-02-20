from django.urls import path
from django.conf.urls import url
from django.views import generic
from rockument.apps.sponge.models import App

urlpatterns = [
    url(
        r"^about/$",
        generic.TemplateView.as_view(template_name="default/about.html"),
        name="about",
    ),
    url(
        r"^$",
        generic.ListView.as_view(model=App, template_name='default/home.html'),
        name="home",
    ),
]