from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
#Import category model
from rango.models import Category
from rango.models import Page
from django.http import HttpResponse



def encode_url(str):
	return str.replace(' ', '_').lower()

def decode_url(str):
    return str.replace('_', ' ').capitalize()


def index(request):
    context = RequestContext(request)
    # Query the database for a list of ALL categories currently stored.
    # Order by the number of likes and show the top five anyway.
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    # Loop through each category returned, creating a URL attribute.
    # The attribute stores an encoded URL (spaces replaced by underscores).
    for category in category_list:
            category.url = encode_url(category.name)

	# Work out the top 5 pages (in terms of views) across all categories.
    page_list = Page.objects.order_by('-views')[:5]
    context_dict['pages'] = page_list

    # Render the response and send it back!
    return render_to_response('rango/index.html', context_dict, context)


#Creating view
def about(request):
    return HttpResponse("Rango say this is the about page <br/> <a href='/rango'>Index</a>")


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None

    return render(request, 'rango/category.html', context_dict)




