from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from django_sftpbrowser.views import browse_page

from django.utils import translation
from django.utils.translation import trans_real


# Create your tests here.
class BrowsePageTest(TestCase):
    def test_browse_url_resolves_to_browse_page(self):
        # self.client.get('browse/')
        lg = trans_real.get_language()
        lg2 = translation.get_language_from_path('https://localhost:8000/')
        trans_real.activate(lg)
        found = resolve('browse/')
        self.assertEqual(found.func, browse_page)

    def test_browse_page_returns_correct_html(self):
        request = HttpRequest()
        response = browse_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('elcome', html)
        self.assertTrue(html.endswith('</html>'))

