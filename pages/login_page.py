from lib.page import Page
from selenium.webdriver.common.by import By

class LoginPage(Page):
    pass

LoginPage.INPUT.LOGIN = (By.NAME, "login")
LoginPage.INPUT.PASSWORD = (By.NAME, "password")
LoginPage.INPUT.TERMINAL = (By.NAME, "terminal")
LoginPage.BUTTON.LOGIN = (By.XPATH, "//button[@class='btn-login mat-primary mat-raised-button']")
