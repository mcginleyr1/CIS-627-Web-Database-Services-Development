from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.index, name="Index"),
	url(r'^search', views.search, name="Search"),
	url(r'^')
]