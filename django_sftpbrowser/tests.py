from django.test import TestCase

SERVER_URL = 'https://localhost:8000'


# Create your tests here.
class BrowsePageTest(TestCase):
    def test_browse_page_returns_correct_html(self):
        response = self.client.get(f'{SERVER_URL}/en/browse/')
        self.assertTemplateUsed(response, 'browse.html')

    def test_browse_page_returns_content_at_root(self):
        response = self.client.get(f'{SERVER_URL}/en/browse/')
        self.fail('Not implemented yet. Finish this!')

    def test_browse_page_returns_content_at_folder(self):
        response = self.client.get(f'{SERVER_URL}/en/browse/upload')
        self.assertTemplateUsed(response, 'browse.html')
        self.fail('Not implemented yet. Finish this!')
