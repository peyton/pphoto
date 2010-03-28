import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Message(models.Model):
    name           = models.CharField(max_length=120, editable=False)
    email          = models.CharField(max_length=320, editable=False)
    body           = models.TextField(editable=False, verbose_name=_("Message"))
    ip             = models.IPAddressField(default="127.0.0.1", editable=False, \
        verbose_name = _("IP Address"))
    created_date   = models.DateTimeField(default=datetime.datetime.now(), \
        editable=False, verbose_name=_("Created on"))
    