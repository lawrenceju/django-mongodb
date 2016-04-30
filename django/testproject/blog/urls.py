from django.conf.urls import include, url
from django.contrib import admin
from . import views 

urlpatterns = [
	url(r'^(search/$)',views.getExten,name='getExten'),
	url(r'^$', views.index,name='index'),
]