import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
# from django.test import LiveServerTestCase

MAX_WAIT = 10


class NewVisitorTest(unittest.TestCase):  # LiveServerTestCase
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    @staticmethod
    def wait_for(fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def check_if_row_entries_in_list(self):
        listing = self.browser.find_element_by_css_selector('ul#current_folder_content')
        rows = listing.find_elements_by_css_selector('li')
        self.assertTrue(len(rows) > 0)

    def check_if_browse_option_exists(self):
        start_time = time.time()
        while True:
            try:
                self.assertTrue(any('rowse' in elem.text
                                    for elem in
                                    self.browser.find_elements_by_tag_name('a'))
                                )
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_access_the_web_and_its_contents(self):
        # Corelli has heard about a superb web site for sharing sheet music. He goes to check its homepage
        self.browser.get('http://localhost:8000/accounts/login')
        # alternative without DB users
        # self.browser.get(self.live_server_url)

        # The user notices the name of the web site
        self.assertIn('Sign In', self.browser.title)

        # The "browse" option is not up there yet
        self.assertFalse(any('rowse' in elem.text
                             for elem in
                             self.browser.find_elements_by_tag_name('a'))
                        )

        # He enters a username and a password. Then tries to log-in
        user_input = self.browser.find_element_by_id('id_login')
        passw_input = self.browser.find_element_by_id('id_password')

        # TODO Use template or make this not language dependent
        self.assertEqual(user_input.get_attribute('placeholder'), 'Username')
        self.assertEqual(passw_input.get_attribute('placeholder'), 'Password')
        # ENDTODO Use template or make this not language dependent

        user_input.send_keys('dummy')
        passw_input.send_keys('lamepass')
        passw_input.send_keys(Keys.ENTER)

        # The "browse" option is now up there
        self.check_if_browse_option_exists()

        # The page now shows a welcome image and message with an invitation
        # to go to the browse page where you can look for the sheet music
        welcome_msg = self.browser.find_element_by_id('welcome_msg')
        self.assertTrue(welcome_msg is not None)

        # Page redirects to the browse page or user requests for the browse page
        self.browser.get('http://localhost:8000/browse')

        # Now he can see the root content for the sheet music server
        # The main listing
        folder_listing = self.wait_for(lambda: self.browser.find_element_by_css_selector('ul#current_folder_content'))
        self.assertTrue(folder_listing is not None)
        #... and the files and subdirectories
        entries_list = self.browser.find_element_by_css_selector('ul#current_folder_content li')
        self.assertTrue(entries_list is not None and len(entries_list))

        # He tries to download the first file README.txt
        self.fail('Finish the test!')

        # If necessary, he goes back to the browse page and then accesses
        # the sheet_music folder

        # He can see now the content of the sheet_folder and the url is
        # reflecting the present working directory

        # Happy about having found such a wonderful website resource,
        # he quits for coming back later
