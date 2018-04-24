from lib.page import Page
from selenium.webdriver.common.by import By

class LoginPage(Page):
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.INPUT.LOGIN = (By.NAME, "login")
        self.INPUT.PASSWORD = (By.NAME, "password")
        self.INPUT.TERMINAL = (By.NAME, "terminal")
        self.BUTTON.LOGIN = (By.XPATH, "//button[@class='btn-login mat-primary mat-raised-button']")
