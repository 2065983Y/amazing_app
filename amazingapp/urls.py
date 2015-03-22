from django.conf.urls import patterns, url
from amazingapp import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^builders/', views.builders, name='builders'),
	url(r'^solvers/', views.solvers, name='solvers'),
	url(r'^mazes/', views.mazes, name='mazes'),
)