from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("My spidey sense is tingling")

def about(request):
    return HttpResponse("So you want to know all about Spidey, Eh!")