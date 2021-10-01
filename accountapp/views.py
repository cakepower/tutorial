from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from accountapp.models import HelloWorld

def index(request):
    return render(request, "shoppingM/index.html")

def index_m(request):
    return render(request, "shoppingM/index_m.html")

def hello_world(request):
#    global new_hello_world
    
    if request.method == "POST":
        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
        
        hello_world_list = HelloWorld.objects.all()
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/base.html', context={'hello_world_list': hello_world_list})

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'



def login(request):
        return render(request, 'accountapp/login.html')

def create(request):
        return render(request, 'accountapp/create.html')
