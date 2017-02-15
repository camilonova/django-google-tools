from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class AnalyticsCode(models.Model):
    site = models.OneToOneField(Site, verbose_name=_('site'))
    code = models.CharField(_('code'), max_length=100)
    speed = models.BooleanField(verbose_name=_('track speed'), default=False)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ('site', 'code')
        verbose_name = _('analytics code')
        verbose_name_plural = _('analytics codes')


@python_2_unicode_compatible
class SiteVerificationCode(models.Model):
    site = models.OneToOneField(Site, verbose_name=_('site'))
    code = models.CharField(_('code'), max_length=100)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ('site', 'code')
        verbose_name = _('site verification code')
        verbose_name_plural = _('site verification codes')
