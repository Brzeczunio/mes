#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from datetime import datetime
from selenium import webdriver
from lib.test import Test
from functools import wraps
from loggers.logger import Logger
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.add_production_page import AddProductionPage
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

def log(func):
    @wraps(func)
    def logging(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except (Exception, WebDriverException, TimeoutException) as e:
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.logger.take_screenshot(self.driver, 'error-%s' % now)
            self.logger.save_log('error-%s' % now, e)
    return logging

class Test(Test, unittest.TestCase):
    @log
    def test_1_login(self):
        loginPage = LoginPage(self.driver)
        loginPage.wait_for_unblock_ui()
        loginPage.set_text_element(loginPage.INPUT.TERMINAL, "qmes")
        loginPage.user_click_element(loginPage.INPUT.LOGIN)
        loginPage.set_text_element(loginPage.INPUT.LOGIN, "oper")
        loginPage.set_text_element(loginPage.INPUT.PASSWORD, "oper")
        loginPage.user_click_element(loginPage.BUTTON.LOGIN)
        mainPage = MainPage(self.driver)
        mainPage.wait_for_unblock_ui()
        mainPage.user_click_element(mainPage.BUTTON.MENU)
        self.assertEqual(u'oper oper', mainPage.get_text_element(mainPage.INFO.OPERATOR))

    @log
    def test_2_add_production(self):
        mainPage = MainPage(self.driver)
        mainPage.wait_for_unblock_ui()
        mainPage.find_element(mainPage.BREADCRUMB.RESOURCES)
        mainPage.wait_for_unblock_ui()
        mainPage.user_click_element(mainPage.BUTTON.ACTION)
        mainPage.user_click_element(mainPage.BUTTON.ADD_PRODUCTION)
        addProductionPage = AddProductionPage(self.driver)
        mainPage.wait_for_unblock_ui()
        addProductionPage.set_text_element(addProductionPage.INPUT.ADD_PRODUCTION, "2")
        addProductionPage.user_click_element(addProductionPage.BUTTON.ADD_PRODUCTION)
        mainPage.wait_for_unblock_ui()
        self.assertEqual(u'Udało się!', mainPage.get_text_element(mainPage.MESSAGE.SUCCESS))

    @log
    def test_3_logout(self):
        loginPage = LoginPage(self.driver)
        mainPage = MainPage(self.driver)
        mainPage.wait_for_unblock_ui()
        mainPage.find_element(mainPage.BREADCRUMB.RESOURCES)
        mainPage.wait_for_unblock_ui()
        mainPage.user_click_element(mainPage.BUTTON.MENU)
        mainPage.wait_for_unblock_ui()
        mainPage.user_click_element(mainPage.BUTTON.LOGOUT)
        self.assertEqual(u'Zaloguj', loginPage.get_text_element(mainPage.BUTTON.LOGIN))

if __name__ == '__main__':
    unittest.main(verbosity=2)
