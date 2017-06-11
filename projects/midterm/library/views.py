from django.shortcuts import render
from django.core.urlresolvers import reverse

def index(request):
	return render(request, 'library/index.html', {})