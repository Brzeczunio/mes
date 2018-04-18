# -*- coding: utf-8 -*-

import os
import shutil
import unittest
from selenium import webdriver
from loggers.logger import Logger
from selenium.webdriver.chrome.options import Options

class Test(object):
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        self.logger = Logger('logs/', 'screenshots/')
        self.getChromeOptions()

    '''Do zmiany! Na strzelanie do API po token'''
    def getChromeOptions(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument(self.set_user_profile_with_clear())

    def set_user_profile_with_clear(self, user_profile='profile/'):
        path = os.path.abspath(user_profile)
        if not os.path.exists(path):
            os.mkdir(path)
        else:
            shutil.rmtree(path, ignore_errors=True)
        user_profile = 'user-data-dir=%s' % path
        return user_profile

    def setUp(self):
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        self.driver.maximize_window()
        self.driver.get('http://192.168.1.63:777')

    def tearDown(self):
        self.driver.quit()
