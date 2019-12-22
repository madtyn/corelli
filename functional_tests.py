import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_access_the_web_and_its_contents(self):
        # Corelli has heard about a superb web site for sharing sheet music. He goes to check its homepage
        self.browser.get('http://localhost:8000/accounts/login')

        # The user notices the name of the web site
        self.assertIn('Sign In', self.browser.title)

        # The "browse" option is not up there yet
        self.assertFalse('rowse' in (elem.text
                                     for elem in
                                     self.browser.find_elements_by_tag_name('a'))
                         )

        # He enters a username and a password. Then tries to log-in
        user_input = self.browser.find_element_by_id('id_login')
        passw_input = self.browser.find_element_by_id('id_password')

        # TODO Use template or make this not language dependent
        self.assertEqual(user_input.get_attribute('placeholder'), 'Username')
        self.assertEqual(passw_input.get_attribute('placeholder'), 'Password')
        # TODO Use template or make this not language dependent

        user_input.send_keys('dummy')
        passw_input.send_keys('dummy')
        passw_input.send_keys(Keys.ENTER)

        # We wait for the new page
        time.sleep(6)

        # The "browse" option is now up there
        self.assertTrue('rowse' in (elem.text
                                    for elem in
                                    self.browser.find_elements_by_tag_name('a'))
                        )

        # The page now shows a welcome image and message with an invitation
        # to go to the browse page where you can look for the sheet music
        welcome_msg = self.browser.find_element_by_id('#welcome_msg')
        self.assertTrue(welcome_msg is not None)

        # He goes to the browse page
        self.fail('Finish the test!')

        # Now he can see the root content for the sheet music server

        # He tries to download the first file README.txt

        # If necessary, he goes back to the browse page and then accesses
        # the sheet_music folder

        # He can see now the content of the sheet_folder and the url is
        # reflecting the present working directory

        # Happy about having found such a wonderful website resource,
        # he quits for coming back later


if __name__ == '__main__':
    unittest.main()
