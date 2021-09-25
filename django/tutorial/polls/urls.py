from django.urls import path
from django.contrib import admin
from polls import views 

from . import views

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.main),
        #path('', views.index, name='index'),
        ]




