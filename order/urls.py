from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from order.forms import OrderWizard, ContactInfoForm, ProductInfoForm
from order.views import order_view

urlpatterns = patterns('',
    url(r'^$', OrderWizard([ProductInfoForm, ContactInfoForm]), {}, 'order_form'),
    url(r'^completed/$', direct_to_template, 
        { 'template': 'order/order_form_sent.html' },
        'order_form_sent'),
)