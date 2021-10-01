from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView


def index(request):
    return render(request, "shoppingM/index.html")

def index_m(request):
    return render(request, "shoppingM/index_m.html")