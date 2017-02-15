from __future__ import absolute_import

from django.conf import settings
from django import template
from django.contrib.sites.models import Site
from django.template import loader, Context

from googletools.models import AnalyticsCode, SiteVerificationCode

register = template.Library()


class AnalyticsCodeNode(template.Node):

    def __init__(self, site):
        self.site = site
        self.template = 'googletools/analytics_code.html'
        self.enabled = getattr(settings, 'GOOGLETOOLS_ENABLED', not settings.DEBUG)
        try:
            self.code = AnalyticsCode.objects.get(site=self.site)
        except AnalyticsCode.DoesNotExist:
            self.code = None

    def render(self, context):
        if not self.enabled or not self.code:
            return ''

        t = loader.get_template(self.template)

        return t.render(Context({
            'analytics_code': self.code,
        }))


class SiteVerificationCodeNode(template.Node):

    def __init__(self, site):
        self.site = site
        self.template = 'googletools/site_verification_code.html'
        self.enabled = getattr(settings, 'GOOGLETOOLS_ENABLED', not settings.DEBUG)
        try:
            self.code = SiteVerificationCode.objects.get(site=self.site)
        except SiteVerificationCode.DoesNotExist:
            self.code = None

    def render(self, context):
        if not self.enabled or not self.code:
            return ''

        t = loader.get_template(self.template)

        return t.render(Context({
            'site_verification_code': self.code,
        }))


@register.tag
def analytics_code(parser, token):
    """
    Get the analytics code for the current site::

        {% analytics_code %}

    Returns an empty string when no code could be found.
    """
    try:
        token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError('%r does not take any arguments' % token.contents.split()[0])

    return AnalyticsCodeNode(site=Site.objects.get_current())


@register.tag
def site_verification_code(parser, token):
    """
    Get the site verification code for the current site::

        {% site_verification_code %}

    Returns an empty string when no code could be found.
    """
    try:
        token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError('%r does not take any arguments' % token.contents.split()[0])

    return SiteVerificationCodeNode(site=Site.objects.get_current())
