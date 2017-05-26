from django.conf.urls import url
from dailyplanet import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
]
