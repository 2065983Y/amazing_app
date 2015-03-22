from django.conf.urls import patterns, url
from amazingapp import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^/mazes$', views.mazes, name='mazes'),
    url(r'^/solve$', views.pickMaze, name='mazePicker'),
    url(r'^/solve/(?P<maze_name>[\w\-]+)/$', views.solveMaze, name='solveMaze'),
    url(r'^/create/$', views.createMaze, name='createMaze'),
)