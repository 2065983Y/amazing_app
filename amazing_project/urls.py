from django.conf.urls import patterns, include, url
from django.contrib import admin
from amazingapp import views
from registration.backends.simple.views import RegistrationView
from django.contrib.auth import views as auth_views



class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/mazeapp/add_profile'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'amazing_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^mazeapp/S', include("amazingapp.urls")),
    url(r'^$', views.index),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/',include('registration.backends.simple.urls')),)
