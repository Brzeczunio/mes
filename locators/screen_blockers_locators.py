# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

class ScreenBlokersLocators(object):
    SCREEN_BLOKER         = (By.XPATH, "//div[@class='ui-blockui ui-widget-overlay ui-blockui-document']")
