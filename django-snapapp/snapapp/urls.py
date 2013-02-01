from django.conf.urls import patterns, url

from snapapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<album_id>\d+)/$', views.index, name='index'),
    url(r'^api/$', views.api, name='api'),
    url(r'^api/(?P<album_id>\d+)/$', views.api, name='api'),
)
