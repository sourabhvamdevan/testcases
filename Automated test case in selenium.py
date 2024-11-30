import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class LogIn(unittest.TestCase):

    def setUp(self):
        
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        
        self.driver.get('https://www.hudl.com')
        self.driver.implicitly_wait(10)

    def test_login_button_present(self):
        
        try:
            assert self.driver.find_element_by_link_text('Log in')
        except NoSuchElementException as e:
            print(e)
            raise

    def test_navigate_to_login_page(self):
        
        self.log_in = self.driver.find_element_by_link_text('Log in')
        self.log_in.click()
        self.driver.implicitly_wait(10)
        try:
            assert self.driver.current_url == 'https://www.hudl.com/login'
        except AssertionError as e:
            print(e)
            raise

    def test_valid_login(self):
        
        self.log_in = self.driver.find_element_by_link_text('Log in')
        self.log_in.click()
        self.driver.implicitly_wait(10)
        try:
            assert self.driver.current_url == 'https://www.hudl.com/login'
        except AssertionError as e:
            print(e)
            raise

        
        self.username_bar = self.driver.find_element_by_name('username')
        self.username_bar.clear()
        self.username_bar.send_keys()

       
        self.password_bar = self.driver.find_element_by_name('password')
        self.password_bar.clear()
        self.password_bar.send_keys()

        
        self.log_in_button = self.driver.find_element_by_id('logIn')
        self.log_in_button.click()

       
        try:
            self.page_title = WebDriverWait(self.driver, 10).until(EC.url_matches('https://www.hudl.com/home'))
        except TimeoutError as e:
            print(e)
            raise

        
        try:
            assert self.driver.current_url == 'https://www.hudl.com/home'
        except AssertionError as e:
            print(e)
            raise

    def test_invalid_login(self):
       
        self.log_in = self.driver.find_element_by_link_text('Log in')
        self.log_in.click()
        self.driver.implicitly_wait(10)
        try:
            self.driver.implicitly_wait(10)
            assert self.driver.current_url == 'https://www.hudl.com/login'
        except AssertionError as e:
            print(e)
            raise

       
        self.username_bar = self.driver.find_element_by_name('username')
        self.username_bar.clear()
        self.username_bar.send_keys()

        
        self.password_bar = self.driver.find_element_by_name('password')
        self.password_bar.clear()

        
        self.log_in_button = self.driver.find_element_by_id('logIn')
        self.log_in_button.click()

        
        try:
            assert self.driver.find_element_by_xpath("//div[contains(@class, 'login-error')]")
        except AssertionError as e:
            print(e)
            raise

    def test_remember_me(self):
       
        self.log_in = self.driver.find_element_by_link_text('Log in')
        self.log_in.click()
        self.driver.implicitly_wait(10)
        try:
            assert self.driver.current_url == 'https://www.hudl.com/login'
        except AssertionError as e:
            print(e)
            raise

        
        self.username_bar = self.driver.find_element_by_name('username')
        self.username_bar.clear()
        self.username_bar.send_keys()

       
        self.password_bar = self.driver.find_element_by_name('password')
        self.password_bar.clear()
        self.password_bar.send_keys()

       
        self.log_in_button = self.driver.find_element_by_id('logIn')
        self.log_in_button.click()

        
        try:
            self.page_title = WebDriverWait(self.driver, 10).until(EC.url_matches('https://www.hudl.com/home'))
        except TimeoutError as e:
            print(e)
            raise

        
        try:
            assert self.driver.current_url == 'https://www.hudl.com/home'
        except AssertionError as e:
            print(e)
            raise

        
        self.driver.find_element_by_xpath("//div[contains(@class, 'hui-globalusermenu')]").click()
        self.driver.find_element_by_xpath("//a[contains(@data-qa-id, 'webnav-usermenu-logout')]").click()

        
        try:
            assert self.driver.current_url == 'https://www.hudl.com/'
        except AssertionError:
            print('Incorrect Page Loaded')

        
        self.log_in = self.driver.find_element_by_link_text('Log in')
        self.log_in.click()
        self.driver.implicitly_wait(10)
        try:
            assert self.driver.current_url == 'https://www.hudl.com/login'
        except AssertionError as e:
            print(e)
            raise

       
        self.username_bar = self.driver.find_element_by_name('username')
        try:
            assert self.username_bar.get_attribute('value') == ''
        except AssertionError as e:
            print(e)
            raise

    def tearDown(self):
       
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)


