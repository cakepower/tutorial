from django.urls.resolvers import URLPattern
from django.urls import path, include
from .import views

app_name = "snapshot"

urlpatterns = [
    path('index', views.index),
]