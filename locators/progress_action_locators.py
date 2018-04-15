# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

class ProgressActionLocators(object):
    PROGRESS_SPINNER      = (By.XPATH, "//mat-progress-spinner[@class='mat-progress-spinner mat-primary mat-progress-spinner-indeterminate-animation']")
