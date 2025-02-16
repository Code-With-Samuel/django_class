from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def view_1(request):
    return render(request, 'home/index.html')

def view_2(request):
    return HttpResponse("<h1> Welcome to django server view 2.</h1>")
