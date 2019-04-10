##############################################################
#author:sunny,version:1.0, date:4/4/2019
#history:
#function:
##############################################################
#basepage.py
#coding= utf-8

import pytest
from selenium import webdriver

class BasePage(object):

    def __init__(self,driver):
        self.driver = driver

    def get_source(self):
        return self.driver.page_source