from lib.page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):
    def __init__(self, driver):
        super(MainPage, self).__init__(driver)
        self.BUTTON.MENU = (By.XPATH, "//button[@class='menu-button-fab mat-mini-fab mat-accent' or @class='mat-mini-fab mat-primary']")
        self.INFO.OPERATOR = (By.XPATH, "//div[@class='info']/h2")
        self.MESSAGE.SUCCESS = (By.XPATH, "//span[@class='ui-growl-title']")
        self.BUTTON.LOGOUT = (By.XPATH, "//div[@class='glyphs ic_mw_logout']")
        self.BUTTON.ACTION = (By.XPATH, "//button[@class='mes-color mat-fab mat-accent']")
        self.BUTTON.ADD_PRODUCTION = (By.XPATH, "//button[@class='mes-color mat-mini-fab mat-accent fab-action-item ng-star-inserted']/span/mat-icon[@class='mat-icon mes-icon material-icons ic_mw_cartadd']")
        self.BREADCRUMB.RESOURCES = (By.XPATH, "//div[text()='Zasoby']")
