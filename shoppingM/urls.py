from django.urls.resolvers import URLPattern
from django.urls import path, include
from accountapp.views import hello_world, AccountCreateView
from django.contrib.auth.views import LoginView, LogoutView
from .import views

app_name = "shoppingM"

urlpatterns = [
    path('index', views.index),
    path('index_m', views.index_m),
]