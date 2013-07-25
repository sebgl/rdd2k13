from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from rdd2013.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', homepage),
    # Examples:
    # url(r'^$', 'rdd2013.views.home', name='home'),
    # url(r'^rdd2013/', include('rdd2013.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
