# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

class AddProductionPageLocators(object):
    ADD_PRODUCTION_INPUT  = (By.XPATH, "//input[@formcontrolname='quantity']")
    ADD_PRODUCTION_BUTTON = (By.XPATH, "//button[@class='image-button mat-raised-button' and @type='submit']/span/div/mat-icon[@class='mat-icon mes-icon material-icons ic_mw_addbutton']")
