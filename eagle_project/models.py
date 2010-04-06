import datetime

from django.db import models
from django.template import Context, Template
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel

ROLE_CHOICES = (
    (0, _('Project Leader')),
    (1, _('Scout Leader')),
    (2, _('Scout')),
)

class Participant(TimeStampedModel):
    name        = models.CharField(max_length=50)
    email       = models.EmailField(blank=True)
    role        = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)
    slug        = AutoSlugField(populate_from='name')
    work        = models.ManyToManyField('eagle_project.Work', blank=True, null=True)
    # donations   
    
    def get_total_hours(self):
        pass
    
    def __unicode__(self):
        """
        Make the model human readable.
        """
        return '%s, %s' % (self.name, self.get_role_display())
    
    class Meta:
        ordering = ('created',)
        get_latest_by = 'created'
    
class Work(TimeStampedModel):
    title       = models.CharField(max_length=100)
    slug        = AutoSlugField(populate_from='title')
    hours       = models.FloatField()
    description = models.TextField()
    date        = models.DateField()
    
    def __unicode__(self):
        """
        Make the model human readable.
        """
        t = Template("{{ title }}, {{ hours }} hour{{ hours|pluralize }}")
        c = Context({'title': self.title, 'hours': self.hours})
        return t.render(c)
    
    class Meta:
        ordering = ('date',)
        get_latest_by = 'date'
        verbose_name_plural = "Work"

# class Donation(TimeStampedModel):
#     title       = models.CharField(max_length=100)
#     slug        = AutoSlugField(populate_from='title')
#     amount      = models.FloatField()
#     description = models.TextField()
#     date        = models.DateField()
#     
#     class Meta:
#         [-]