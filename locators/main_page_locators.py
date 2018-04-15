# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

class MainPageLocatars(object):
    MENU_BUTTON           = (By.XPATH, "//button[@class='menu-button-fab mat-mini-fab mat-accent' or @class='mat-mini-fab mat-primary']")
    OPERATOR_INFO         = (By.XPATH, "//div[@class='info']/h2")
    LOGOUT_BUTTON         = (By.XPATH, "//div[@class='glyphs ic_mw_logout']")
    ACTION_BUTTON         = (By.XPATH, "//button[@class='mes-color mat-fab mat-accent']")
    ADD_PRODUCTION_BUTTON = (By.XPATH, "//button[@class='mes-color mat-mini-fab mat-accent fab-action-item ng-star-inserted']/span/mat-icon[@class='mat-icon mes-icon material-icons ic_mw_cartadd']")
    SUCCESS_MESSAGE       = (By.XPATH, "//span[@class='ui-growl-title']")
