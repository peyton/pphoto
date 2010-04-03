from django.conf.urls.defaults import *

template_subdirectory = 'common/' # template subdirectory

urlpatterns = patterns('django.views.generic.simple',
    ('^$',               'direct_to_template', {'template': '%shome.html' % template_subdirectory},
        'home'),
    ('^about/$',         'direct_to_template', {'template': '%sabout.html' % template_subdirectory},
        'about'),
    ('^samples/$',       'direct_to_template', {'template': '%ssamples.html' % template_subdirectory},
        'samples'),
    ('^qanda/$',         'direct_to_template', {'template': '%sqanda.html' % template_subdirectory},
        'qanda'),
)
