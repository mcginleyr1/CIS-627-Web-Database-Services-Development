from django.shortcuts import render
#Import category model
from rango.models import Category
from rango.models import Page
from django.http import HttpResponse

def index(request):
    #Chapter 6 notes
    #Query the DB for a list of ALL categories stored
    #order the categories by numbers. Likes in descending order
    #Retrieve the top 5 only or all if less than 5
    #place the list in the context_dict dictionary so that it can be passed to the template
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    #Return a rendered response to send to the client
    #We make use of the shortcut function to make things easier
    #Note that the first parameter is the template we wish to  use
    return render(request, 'rango/index.html', context_dict)
#Creating view
def about(request):
    return HttpResponse("Rango say this is the about page <br/> <a href='/rango'>Index</a>")

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category_name_slug)

        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None

    return render(request, 'rango/category.html', context_dict)




