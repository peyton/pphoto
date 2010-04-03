from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib.sitemaps import GenericSitemap

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Example:
    # (r'^pandolph/', include('pandolph.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    (r'^order/', include('pphoto.order.urls')),
    (r'^contact/', include('pphoto.contact.urls')),
    
    (r'^', include('pphoto.common.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'^static/(?P<path>.*)$', 'serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        )