import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import AutoSlugField

ROLE_CHOICES = (
    (0, _('Project Leader')),
    (1, _('Scout Leader')),
    (2, _('Scout')),
)

class Participant(models.Model):
    name        = models.CharField(max_length=50)
    email       = models.EmailField(blank=True)
    role        = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)
    slug        = AutoSlugField(populate_from='name')
    created_date= models.DateTimeField(default=datetime.datetime.now(), editable=False, verbose_name=_('Created on'))
    work        = models.ManyToManyField('eagleproject.Work', blank=True, null=True)
    # donations   
    
    def get_total_hours(self):
        pass
    
    class Meta:
        ordering = ['created_date']
        get_latest_by = 'created_date'
    
class Work(models.Model):
    title       = models.CharField(max_length=100)
    slug        = AutoSlugField(populate_from='title')
    hours       = models.FloatField()
    description = models.TextField()
    date        = models.DateField()
    created_date= models.DateTimeField(default=datetime.datetime.now(), editable=False, verbose_name=_('Created on'))
    
    class Meta:
        ordering = ['date']
        get_latest_by = 'date'
        verbose_name_plural = "Work"

# class Donation(models.Model):
#     title       = models.CharField(max_length=100)
#     slug        = AutoSlugField(populate_from='title')
#     amount      = models.FloatField()
#     description = models.TextField()
#     date        = models.DateField()
#     created_date= models.DateTimeField(default=datetime.datetime.now(), editable=False, verbose_name=_('Created on'))
#     
#     class Meta:
#         [-]