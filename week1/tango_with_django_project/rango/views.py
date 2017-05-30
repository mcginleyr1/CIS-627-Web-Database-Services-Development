from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! Visit the <a href='rango/about'>About</a> page")

def about(request):
    return HttpResponse("Rango says there is an about page! Go back to the <a href='/'>Home</a> page")
