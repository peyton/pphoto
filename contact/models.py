import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel

class Message(TimeStampedModel):
    name           = models.CharField(max_length=50)
    from_email     = models.EmailField(max_length=320, verbose_name=_("Email"))
    message        = models.TextField(verbose_name=_("Message"))
    ip             = models.IPAddressField(default="127.0.0.1", verbose_name = _("IP Address"))
    responded_to   = models.BooleanField()
    