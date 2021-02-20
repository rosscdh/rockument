from django.urls import path

from rockument.apps.lens import views


urlpatterns = [
    path('<slug>/', views.RevisionDetailView.as_view()),
    path('<slug>/latest/', views.RevisionDetailView.as_view()),
    path('<slug>/<revision>/', views.RevisionDetailView.as_view()),
]
