from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from mongoadmin import site

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'juannyg.views.home', name='home'),
    url(r'', include('main.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(site.urls)),
)
