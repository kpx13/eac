# -*- coding: utf-8 -*-

from django.contrib import admin
from django.conf import settings
from django.conf.urls.defaults import patterns, include, url

from filebrowser.sites import site
import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.home_page),
    url(r'^page/(?P<page_name>\w+)$' , views.page),
    
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/favicon.ico'}),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),   
)

if settings.DEBUG:
    urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )