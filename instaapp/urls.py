from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
   url(r'^$', views.home, name='home'),
   url(r'^accounts/login', views.login_view, name='login'),
   url(r'^accounts/logout', views.logout_view, name='logout'),
)