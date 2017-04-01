from django.shortcuts import render
from django.http import HttpResponse

from rango.models import Category, Page

def index(request):
    categories = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': categories}
    return render(request, 'rango/index.html', context_dict)


def show_category(request, category_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_slug)
        pages = Page.objects.filter(category=category)
        context_dict = {
            'pages': pages,
            'category': category
        }
    except Category.DoesNotExist as e:
        context_dict = {'pages': None, 'category': None}
    return render(request, 'rango/category.html', context_dict)
