#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from datetime import datetime
from selenium import webdriver
from lib.test import Test
from loggers.logger import Logger
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.add_production_page import AddProductionPage
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

def Log(fun):
    def Logging(self, *args, **kwargs):
        try:
            return fun(self, *args, **kwargs)
        except (Exception, WebDriverException, TimeoutException) as e:
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.logger.take_screenshot(self.driver, 'error-%s' % now)
            self.logger.save_log('error-%s' % now, e)
    return Logging

class Test(Test, unittest.TestCase):
    @Log
    def test_1_Login(self):
        loginPage = LoginPage(self.driver)
        loginPage.set_text_element(loginPage.INPUT.TERMINAL, "qmes")
        loginPage.click_element(loginPage.INPUT.LOGIN)
        loginPage.set_text_element(loginPage.INPUT.LOGIN, "oper")
        loginPage.set_text_element(loginPage.INPUT.PASSWORD, "oper")
        loginPage.click_element(loginPage.BUTTON.LOGIN)
        mainPage = MainPage(self.driver)
        mainPage.click_element(mainPage.BUTTON.MENU)
        self.assertEqual(u'oper oper', mainPage.get_text_element(mainPage.INFO.OPERATOR))

    @Log
    def test_2_Add_Production(self):
        loginPage = LoginPage(self.driver)
        mainPage = MainPage(self.driver)
        mainPage.click_element(loginPage.BUTTON.ACTION)
        mainPage.click_element(loginPage.BUTTON.ADD_PRODUCTION)
        addProductionPage = AddProductionPage(self.driver)
        addProductionPage.set_text_element(addProductionPage.INPUT.ADD_PRODUCTION, "2")
        addProductionPage.set_text_element(addProductionPage.BUTTON.ADD_PRODUCTION, "2")
        self.assertEqual(u'Udało się!', mainPage.get_text_element(mainPage.MESSAGE.SUCCESS))

    @Log
    def test_3_Logout(self):
        loginPage = LoginPage(self.driver)
        mainPage = MainPage(self.driver)
        mainPage.click_element(mainPage.BUTTON.MENU)
        mainPage.click_element(mainPage.BUTTON.LOGOUT)
        self.assertEqual(u'Zaloguj', loginPage.get_text_element(mainPage.BUTTON.LOGIN))

if __name__ == '__main__':
    unittest.main(verbosity=2)
