from django.urls.resolvers import URLPattern
from django.urls import path, include
from accountapp.views import hello_world, AccountCreateView
from django.contrib.auth.views import LoginView, LogoutView
from .import views

app_name = "accountapp"

urlpatterns = [
    path('', hello_world, name = 'hello_world' ),
    path('hello_world', hello_world, name = 'hello_world' ),
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('create/', AccountCreateView.as_view(), name='create'),
    path('index', views.index),
    path('index_m', views.index_m),
]
