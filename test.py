#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from datetime import datetime
from selenium import webdriver
from base.base import TestBase
from loggers.logger import Logger
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.add_production_page import AddProductionPage
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *

class Test(TestBase, unittest.TestCase):
    def test_1_Login(self):
        try:
            driver = self.driver
            loginPage = LoginPage(driver)
            loginPage.enter_login("oper")
            loginPage.enter_password("oper")
            loginPage.enter_terminal("qmes")
            loginPage.click_login_button()

            mainPage = MainPage(driver)
            mainPage.click_menu_button()
            self.assertEqual(u'oper oper', mainPage.get_operator_info())

        except (Exception, WebDriverException, TimeoutException) as e:
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.logger.take_screenshot(driver, 'error-%s' % now)
            self.logger.save_log('error-%s' % now, e)

    def test_2_Add_Production(self):
        try:
            driver = self.driver
            loginPage = LoginPage(driver)
            mainPage = MainPage(driver)
            mainPage.click_action_button()
            mainPage.click_action_add_production_button()
            addProductionPage = AddProductionPage(driver)
            addProductionPage.enter_production("2")
            addProductionPage.click_add_production_button()
            self.assertEqual(u'Udało się!', mainPage.get_success_message())
        except (Exception, WebDriverException, TimeoutException) as e:
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.logger.take_screenshot(driver, 'error-%s' % now)
            self.logger.save_log('error-%s' % now, e)

    def test_3_Logout(self):
        try:
            driver = self.driver
            loginPage = LoginPage(driver)
            mainPage = MainPage(driver)
            mainPage.click_menu_button()
            mainPage.click_logout_button()
            self.assertEqual(u'Zaloguj', loginPage.get_text_login_button())
        except (Exception, WebDriverException, TimeoutException) as e:
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.logger.take_screenshot(driver, 'error-%s' % now)
            self.logger.save_log('error-%s' % now, e)

if __name__ == '__main__':
    unittest.main(verbosity=2)
