from django.urls import path

from rockument.apps.lens import views


urlpatterns = [
    path('<slug>/', views.RevisionDetailView.as_view(), name="app_detail"),
    path('<slug>/<revision>/', views.RevisionDetailView.as_view(), name="app_revision"),
]
