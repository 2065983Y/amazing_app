from django.conf.urls import patterns, url
from amazingapp import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^/builders/', views.builders, name='builders'),
    url(r'^/solvers/', views.solvers, name='solvers'),
    url(r'^/mazes/', views.mazes, name='mazes'),
    url(r'^/solve$', views.pickMaze, name='mazePicker'),
    url(r'^/solve/(?P<maze_name>[\w\-]+)/$', views.solveMaze, name='solveMaze'),
    url(r'^/create/$', views.create_maze, name='createMaze'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^profile/$', views.edit_profile, name='profile'),
    url(r'add_profile/', views.register_profile, name='register_profile'),

)