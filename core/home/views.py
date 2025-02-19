from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def view_1(request):
    return render(request, 'home/index.html')

def view_2(request):
    return HttpResponse("<h1> Welcome to django server view 2.</h1>")


"""
This can also be done in this way:

from django.http import HttpResponse
from django.template import loader

def view_1(request):
    template = loader.get_template('home/index.html')
    return HttpResponse(template.render())

def view_2(request):
    return HttpResponse("<h1> Welcome to django server view 2.</h1>")

"""



from django.http import HttpResponse
from django.template import loader
from .models import Member

def home(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }

    return HttpResponse(template.render(context,request))