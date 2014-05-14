from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from os.path import dirname
basedir = dirname(__file__)

staticFiles = '%s/newsleter/static/' % basedir
media = '%s/media/' % basedir

from newsletter.views import loginStart

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'detour_news.views.home', name='home'),
    # url(r'^detour_news/', include('detour_news.foo.urls')),
    #static files
    (r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root': staticFiles,'show_indexes': True}),
    (r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root': media,'show_indexes': True}),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #vistas
    url(r'^$',loginStart,name='login'),
    url(r'^news/',include('newsletter.urls')),
)
