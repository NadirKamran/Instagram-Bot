import os
from time import sleep

from selenium import webdriver

insta_user = os.environ['bot_insta_user']
insta_password = os.environ['bot_insta_pwd']

browser = webdriver.Firefox()

browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

sleep(2)

accept_button = browser.find_element_by_xpath("//button[text()='Accept']")
accept_button.click()

sleep(2)

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")
username_input.send_keys(insta_user)
password_input.send_keys(insta_password)

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(5)


browser.close()
