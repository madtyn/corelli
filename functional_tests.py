import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_access_the_web_and_its_contents(self):
        # Corelli has heard about a superb web site for sharing sheet music. He goes to check its homepage
        self.browser.get('http://localhost:8000')

        # The user notices the name of the web site
        assert 'corelli' in self.browser.title, f'Browser title was {self.browser.title}'

        # He enters a username and a password. Then tries to log-in
        self.fail('Finish the test!')

        # The page now shows a welcome image and message with an invitation
        # to go to the browse page where you can look for the sheet music

        # He goes to the browse page

        # Now he can see the root content for the sheet music server

        # He tries to download the first file README.txt

        # If necessary, he goes back to the browse page and then accesses the sheet_music folder

        # He can see now the content of the sheet_folder and the url is reflecting the present working directory

        # Happy about having found such a wonderful website resource, he quits for coming back later


if __name__ == '__main__':
    unittest.main()
