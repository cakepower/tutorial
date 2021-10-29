from django.urls.resolvers import URLPattern
from django.urls import path, include
from accountapp.views import hello_world, AccountCreateView, AccountDetailView
from django.contrib.auth.views import LoginView, LogoutView
from .import views

# app_name = "accountapp"

urlpatterns = [
    path('', views.index ),
    path('hello_world', views.hello_world, name='hello_world'),
    path('samsung', views.hello_world ),
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),   
    path('ikea', views.index),
    path('new', views.new),
]
