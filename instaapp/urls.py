from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
   url(r'^$', views.home, name='home'),
   url(r'^accounts/signup', views.signup_view, name='signup'),
   url(r'^accounts/login', views.login_view, name='login'),
   url(r'^accounts/logout', views.logout_view, name='logout'),
   url(r'^upload/(?P<image_id>\d+)/$', views.upload, name='upload'),
   url(r'^upload/$', views.upload, name='upload'),
)