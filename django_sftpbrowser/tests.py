from django.test import TestCase

SERVER_URL = 'http://localhost:8000'
SFTP_ROOT = '/share/MD0_DATA/Public/corelli_ftp'


# Create your tests here.
class BrowsePageTest(TestCase):
    def goto(self, suffix):
        return self.client.get(f'{SERVER_URL}{suffix}')

    def test_browse_page_returns_correct_html(self):
        response = self.goto('/en/browse/')
        self.assertTemplateUsed(response, 'browse.html')

    def test_browse_page_returns_content_at_root(self):
        response = self.goto('/en/browse/')
        self.assertContains(response, '<li class="file">')
        self.assertContains(response, f'<a class="file" href="{SERVER_URL}/browse/README.txt">README.txt</a>')
        self.assertContains(response, '<li class="folder">')
        self.assertContains(response, f'<a class="folder" href="{SERVER_URL}/browse/sheet_music">sheet_music</a>')

    def test_browse_page_returns_content_at_folder(self):
        response = self.goto('/en/browse/sheet_music')
        self.assertTemplateUsed(response, 'browse.html')
        self.assertContains(response, '<li class="folder">')
        self.assertContains(response, f'<a class="folder" href="{SERVER_URL}/browse/sheet_music/collections">collections</a>')
        self.assertContains(response, '<li class="folder">')
        self.assertContains(response, f'<a class="folder" href="{SERVER_URL}/browse/sheet_music/composers">composers</a>')
