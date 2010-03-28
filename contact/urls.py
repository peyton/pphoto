from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from contact.forms import MessageForm
from contact.views import contact_form

urlpatterns = patterns('',
    url(r'^$', contact_form, {'form_class': MessageForm}, 'contact_form'),
    url(r'^sent/$', direct_to_template, 
        { 'template': 'contact/contact_form_sent.html' },
        'contact_form_sent'),
)