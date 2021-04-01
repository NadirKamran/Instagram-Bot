import os
from time import sleep
from selenium import webdriver

insta_user = os.environ['bot_insta_user']
insta_password = os.environ['bot_insta_pwd']

class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        username_input = browser.find_element_by_css_selector("input[name='username']")
        password_input = browser.find_element_by_css_selector("input[name='password']")
        username_input.send_keys(insta_user)
        password_input.send_keys(insta_password)
        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(5)

class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def go_to_login_page(self):
        accept_button = browser.find_element_by_xpath("//button[text()='Accept']")
        accept_button.click()
        sleep(2)
        return LoginPage(self.browser)

def test_login_page(browser):
    home_page = HomePage(browser)
    login_page = home_page.go_to_login_page()
    login_page.login(insta_user, insta_password)

    errors = browser.find_elements_by_css_selector('#error_message')
    assert len(errors) == 0
    browser.close()

browser = webdriver.Firefox()
browser.implicitly_wait(5)
test_login_page(browser)
