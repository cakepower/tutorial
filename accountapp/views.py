#!/usr/bin/python
# -*- coding: utf-8 -*-

from konlpy.tag import Okt, Kkma, Hannanum
from collections import Counter

kkma = Hannanum()

from django.http.response import HttpResponseForbidden
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from accountapp.models import Blog, Hello, World, Condition
import random
# from accountapp.forms import AccountUpdateForm

j = 0
k = 0

def index(request):
    if request.method == "POST":
        temp = request.POST.get('input_title')
        temp2 = request.POST.get('input_contents')

        new_hello_world = World()
        new_hello_world.title = temp
        new_hello_world.contents = temp2
        new_hello_world.save()
        return HttpResponseRedirect('/')
    else:
        worlds = World.objects.all()
        conditions= Condition.objects.all()
        global j, k
        i, index_n = divmod(j, 21)
        i, index_k = divmod(k, 3)
        condition = conditions[index_n]
        futures = ['바람직한 미래', '있을법한 미래', '예상 밖의 미래']
        future = futures[random.randint(0,2)]
        j += 1
        k += 1

        return render(request, 'accountapp/world.html', context={ 'cond': condition, 'future': future, 'worlds': worlds, 'index_n' : index_n })

def new(request):
    return render(request, 'accountapp/new.html')

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs' : blogs})
    
def hello_world(request):
#    global new_hello_world
    if request.method == "POST":
        temp = request.POST.get('hello_input')
        temp2 = request.POST.get('hello_input2')

        new_hello_world = Hello()
        new_hello_world.text2 = temp
        new_hello_world.text = temp2
        new_hello_world.save()
        
        hello_world_list = Hello.objects.all()
        blogs= Blog.objects.all()
        return HttpResponseRedirect(reverse('hello_world'))
 #       return render(request, 'accountapp/base.html', context={ 'hello_list': hello_world_list, 'blogs':blogs, 'index':index })
    else:
        hello_world_list = Hello.objects.all()
        blogs = Blog.objects.all()
        index_n = random.randint(0, 20)
        blog = blogs[index_n]
        futures = ['바람직한 미래', '있을법한 미래', '예상 밖의 미래']
        future = futures[random.randint(0,2)]
#        for j in range(0, 23):
#            sample = hello_world_list[j]
#            noun = kkma.nouns(sample.text2)
#            for i,v in enumerate(noun):
#                if len(v) < 2:
#                    noun.pop(i)
#            count = Counter(noun)
#
#        noun_list = count.most_common(100)

        return render(request, 'accountapp/base.html', context={ 'hello_list': hello_world_list, 'blogs':blog, 'index':index_n, 'future':future })

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'    
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()
    
    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return super().post(*args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))


class AccountCreateView(DeleteView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

def login(request):
        return render(request, 'accountapp/login.html')

def create(request):
        return render(request, 'accountapp/create.html')

def detail(request):
     return render(request, 'accountapp/detail.html')
