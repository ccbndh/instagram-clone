from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
   url(r'^$', views.home, name='home'),
   url(r'^photo/(?P<image_id>\d+)/$', views.photo_view, name='photo'),
   url(r'^photo/$', views.photo_view, name='photo'),
   url(r'^user/(?P<user_id>\d+)/$', views.user_view, name='user'),
   url(r'^user/$', views.user_view, name='user'),
   url(r'^profile/$', views.profile_view, name='profile'),
   url(r'^search/$', views.search_view, name='search'),
   url(r'^accounts/signup', views.signup_view, name='signup'),
   url(r'^accounts/login', views.login_view, name='login'),
   url(r'^accounts/logout', views.logout_view, name='logout'),
   url(r'^upload/(?P<image_id>\d+)/$', views.upload, name='upload'),
   url(r'^upload/$', views.upload, name='upload'),
)