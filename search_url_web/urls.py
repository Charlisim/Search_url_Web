from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from search_url.models import synology_conf
admin.autodiscover()
admin.site.register(synology_conf)
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'search_url.views.home', name='home'),
    # url(r'^search_url_web/', include('search_url_web.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
