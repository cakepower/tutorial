from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, 'polls/index.html')

#def index(request):
#    return HttpResponse("<h1>Hello, Seungsoo, what's up?.</h1>")

# Create your views here.
