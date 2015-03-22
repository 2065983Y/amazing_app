from django.conf.urls import patterns, url
from amazingapp import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
<<<<<<< HEAD
	url(r'^builders/', views.builders, name='builders'),
	url(r'^solvers/', views.solvers, name='solvers'),
	url(r'^mazes/', views.mazes, name='mazes'),
=======
    url(r'^/mazes$', views.mazes, name='mazes'),
    url(r'^/solve$', views.pickMaze, name='mazePicker'),
    url(r'^/solve/(?P<maze_name>[\w\-]+)/$', views.solveMaze, name='solveMaze')
>>>>>>> 08fa5a13ca0617e56cd77aa1f713ed90c307394a
)