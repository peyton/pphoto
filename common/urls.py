from django.conf.urls.defaults import *

TS = 'common/' # template subdirectory

urlpatterns = patterns('django.views.generic.simple',
    ('^$',               'direct_to_template', {'template': '%shome.html' % TS},
        'home'),
    ('^about/$',         'direct_to_template', {'template': '%sabout.html' % TS},
        'about'),
    ('^samples/$',       'direct_to_template', {'template': '%ssamples.html' % TS},
        'samples'),
    ('^order/$',         'direct_to_template', {'template': '%sorder.html' % TS},
        'order'),
    ('^qanda/$',         'direct_to_template', {'template': '%sqanda.html' % TS},
        'qanda'),
)
