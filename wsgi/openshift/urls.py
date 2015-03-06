from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'openshift.views.home', name='home'),
    # url(r'^openshift/', include('openshift.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'openshift.cofrade.views.home'),
    url(r'^cofradia/$', 'openshift.cofrade.views.nombrecofra'),
    url(r'^paso/$', 'openshift.cofrade.views.nombrepaso'),
    url(r'^contacto/$', 'openshift.cofrade.views.contacto'),
    url(r'^cofradia/(?P<cofradia_id>[0-9]{0,4})/$', 'openshift.cofrade.views.cofradetalle'),
)
