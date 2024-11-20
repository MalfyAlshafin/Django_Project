from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def menu(request):
    template = loader.get_template('menu.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def master(request):
    template = loader.get_template('master.html')
    return HttpResponse(template.render())
