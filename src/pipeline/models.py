from django.db import models
from django.utils.translation import ugettext as _

from . import behaviors


class Application(behaviors.TimeStampedModel, models.Model):
    """
    Contains information about a software application.
    """

    WEB_PLATFORM = 'web'
    DESKTOP_PLATFORM = 'desktop'
    MOBILE_PLATFORM = 'mobile'
    WEB_SERVICE_PLATFORM = 'web service'
    PLATFORM_CHOICES = (
        (WEB_PLATFORM, _('Web')),
        (DESKTOP_PLATFORM, _('Desktop')),
        (MOBILE_PLATFORM, _('Mobile')),
        (WEB_SERVICE_PLATFORM, _('Web Service')),
    )

    VERY_HIGH_CRITICALITY = 'very high'
    HIGH_CRITICALITY = 'high'
    MEDIUM_CRITICALITY = 'medium'
    LOW_CRITICALITY = 'low'
    NONE_CRITICALITY = 'none'
    CRITICALITY_CHOICES = (
        (VERY_HIGH_CRITICALITY, _('Very High')),
        (HIGH_CRITICALITY, _('High')),
        (MEDIUM_CRITICALITY, _('Medium')),
        (LOW_CRITICALITY, _('Low')),
        (NONE_CRITICALITY, _('None')),
    )

    INTERNAL_ORIGIN = 'internal'
    PURCHASED_ORIGIN = 'purchased'
    OPEN_SOURCE_ORIGIN = 'open source'
    ORIGIN_CHOICES = (
        (INTERNAL_ORIGIN, _('Internally Developed')),
        (PURCHASED_ORIGIN, _('Purchased')),
        (OPEN_SOURCE_ORIGIN, _('Open Source')),
    )

    ANALYSIS_LIFECYCLE = 'analysis'
    DESIGN_LIFECYCLE = 'design'
    DEVELOPMENT_LIFECYCLE = 'development'
    TESTING_LIFECYCLE = 'testing'
    DEPLOYMENT_LIFECYCLE = 'deployment'
    MAINTENANCE_LIFECYCLE = 'maintenance'
    LIFECYCLE_CHOICES = (
        (ANALYSIS_LIFECYCLE, _('Analysis')),
        (DESIGN_LIFECYCLE, _('Design')),
        (DEVELOPMENT_LIFECYCLE, _('Development')),
        (TESTING_LIFECYCLE, _('Testing')),
        (DEPLOYMENT_LIFECYCLE, _('Deployment')),
        (MAINTENANCE_LIFECYCLE, _('Maintenance')),
    )

    name = models.CharField(max_length=128, help_text=_('What is the application called?'))
    description = models.TextField(blank=True, help_text=_('What is the application\'s purpose, history, and design?'))
    platform = models.CharField(max_length=11, choices=PLATFORM_CHOICES, help_text=_('Through what medium will the application be utilized?'))
    criticality = models.CharField(max_length=9, choices=CRITICALITY_CHOICES, help_text=_('How important is the application to you?'))
    origin = models.CharField(max_length=11, choices=ORIGIN_CHOICES, help_text=_('Where did the application come from?'))
    lifecycle = models.CharField(max_length=11, choices=LIFECYCLE_CHOICES, help_text=_('What development phase is the application in?'))
    active = models.BooleanField(default=True, help_text=_('Is the application operational?'))

    class Meta:
        get_latest_by = 'modified'
        ordering = ['name']

    def __str__(self):
        return self.name
