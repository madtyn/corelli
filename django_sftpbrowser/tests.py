from django.test import TestCase

SERVER_URL = 'https://localhost:8000'


# Create your tests here.
class BrowsePageTest(TestCase):
    def test_browse_page_returns_correct_html(self):
        response = self.client.get(f'{SERVER_URL}/en/browse/')
        self.assertTemplateUsed(response, 'browse.html')
