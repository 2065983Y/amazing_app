from django.conf.urls import patterns, url
from amazingapp import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^/builders/', views.builders, name='builders'),
    url(r'^/solvers/', views.solvers, name='solvers'),
    url(r'^/mazes/', views.mazes, name='mazes'),
    url(r'^/solve$', views.pickMaze, name='mazePicker'),
    url(r'^/solve/(?P<maze_name>[\w\-]+)/$', views.solveMaze, name='solveMaze'),
    url(r'^/profile$', views.profile, name='profile'),
    url(r'^password_change/$', views.my_password_change, name='password_change'),
    url(r'^password_change/done/$', views.password_change_done, name='password_change_done'),
    url(r'^add_profile/', views.register_profile, name='register_profile'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^/create/$', views.create_maze, name='createMaze'),
)