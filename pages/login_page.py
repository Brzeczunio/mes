from lib.page import Page
from selenium.webdriver.common.by import By

class LoginPage(Page):
    Page.INPUT.LOGIN                      = (By.NAME, "login")
    Page.INPUT.PASSWORD                   = (By.NAME, "password")
    Page.INPUT.TERMINAL                   = (By.NAME, "terminal")
    Page.BUTTON.LOGIN                     = (By.XPATH, "//button[@class='btn-login mat-primary mat-raised-button']")
