##############################################################
# author:sunny,version:1.0, date:4/4/2019
# history:
# function:
##############################################################
# signinpage.py
# coding= utf-8

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from page.basepage import *

class LoginPage(BasePage):

    url = "https://github.com/"

    def login(self,email,pwd):
        self.driver.get(LoginPage.url)
        self.driver.implicitly_wait(2)

        self.driver.find_element_by_css_selector("a[href$='/login']").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("login_field").send_keys(email)
        self.driver.find_element_by_id("password").send_keys(pwd)

        self.driver.find_element_by_name("commit").click()