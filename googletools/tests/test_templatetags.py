from django.contrib.sites.models import Site
from django.template.loader import render_to_string
from django.test import TestCase
from django.test.utils import override_settings

from googletools.templatetags.googletools import AnalyticsCodeNode
from googletools.templatetags.googletools import SiteVerificationCodeNode


class AnalyticsCodeTestCase(TestCase):
    fixtures = ['sites', 'analytics_codes']

    def setUp(self):
        self.site_a = Site.objects.get(pk=1)
        self.site_b = Site.objects.get(pk=2)
        self.correct_out_a = render_to_string('googletools/tests/analytics_code_out_a.html', {})
        self.correct_out_b = render_to_string('googletools/tests/analytics_code_out_b.html', {})

    def test_templatetag(self):
        code_in = render_to_string('googletools/tests/analytics_code_in.html', {})
        self.assertEqual(code_in, self.correct_out_a)

    def test_node_site_a(self):
        node = AnalyticsCodeNode(site=self.site_a)
        self.assertEqual(node.render(None), self.correct_out_a)

    def test_node_site_b(self):
        node = AnalyticsCodeNode(site=self.site_b)
        self.assertEqual(node.render(None), self.correct_out_b)

    @override_settings(DEBUG=True)
    def test_debug(self):
        node = AnalyticsCodeNode(site=self.site_a)
        self.assertEqual(node.render(None), '')

    @override_settings(GOOGLETOOLS_ENABLED=False)
    def test_disabled(self):
        node = AnalyticsCodeNode(site=self.site_a)
        self.assertEqual(node.render(None), '')


class SiteVerificationCodeTestCase(TestCase):
    fixtures = ['sites', 'site_verification_codes']

    def setUp(self):
        self.site_a = Site.objects.get(pk=1)
        self.site_b = Site.objects.get(pk=2)
        self.correct_out_a = render_to_string('googletools/tests/site_verification_code_out_a.html', {})
        self.correct_out_b = render_to_string('googletools/tests/site_verification_code_out_b.html', {})

    def test_templatetag(self):
        code_in = render_to_string('googletools/tests/site_verification_code_in.html', {})
        self.assertEqual(code_in, self.correct_out_a)

    def test_node_site_a(self):
        node = SiteVerificationCodeNode(site=self.site_a)
        self.assertEqual(node.render(None), self.correct_out_a)

    def test_node_site_b(self):
        node = SiteVerificationCodeNode(site=self.site_b)
        self.assertEqual(node.render(None), self.correct_out_b)

    @override_settings(DEBUG=True)
    def test_debug(self):
        node = SiteVerificationCodeNode(site=self.site_a)
        self.assertEqual(node.render(None), '')

    @override_settings(GOOGLETOOLS_ENABLED=False)
    def test_disabled(self):
        node = SiteVerificationCodeNode(site=self.site_a)
        self.assertEqual(node.render(None), '')
