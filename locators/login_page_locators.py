# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    LOGIN                 = (By.NAME, "login")
    PASSWORD              = (By.NAME, "password")
    TERMINAL              = (By.NAME, "terminal")
    LOGIN_BUTTON          = (By.XPATH, "//button[@class='btn-login mat-primary mat-raised-button']")
