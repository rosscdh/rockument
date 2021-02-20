from django.urls import path
from django.conf.urls import url
from django.views import generic
from rockument.apps.sponge.models import App
from rockument.apps.default import views
urlpatterns = [
    url(
        r"^about/$",
        generic.TemplateView.as_view(template_name="default/about.html"),
        name="about",
    ),
    url(
        r"^$",
        views.HomePageView.as_view(),
        name="home",
    ),
]