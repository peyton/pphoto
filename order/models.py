import datetime

from django.contrib.localflavor.us.models import PhoneNumberField, USStateField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel

class Contact(TimeStampedModel):
    name           = models.CharField(max_length=70)
    email          = models.EmailField(max_length=320)
    phone          = PhoneNumberField(blank=True)
    address        = models.CharField(max_length=320, blank=True)
    city           = models.CharField(max_length=100, blank=True)
    state          = USStateField(blank=True)
    zipcode        = models.CharField(max_length=10, blank=True)

class Product(TimeStampedModel):
    kind           = models.CharField(max_length=200)
    quantity       = models.PositiveIntegerField()
    assembly       = models.BooleanField(default=False)

class Order(TimeStampedModel):
    ip             = models.IPAddressField(default="200.200.200.200", verbose_name = _("IP Address"))
    contact        = models.ForeignKey(Contact)
    product        = models.ForeignKey(Product)
    comments       = models.TextField(blank=True)
