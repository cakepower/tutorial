from django.urls.resolvers import URLPattern
from django.urls import path, include
from pragmatic.views import hello_world

app_name = "pragmatic"

urlpatterns = [
    path('', hello_world, name = 'hello_world' ),
]
