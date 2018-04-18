from lib.page import Page
from selenium.webdriver.common.by import By

class AddProductionPage(Page):
    Page.INPUT.ADD_PRODUCTION             = (By.XPATH, "//input[@formcontrolname='quantity']")
    Page.BUTTON.ADD_PRODUCTION            = (By.XPATH, "//button[@class='image-button mat-raised-button' and @type='submit']/span/div/mat-icon[@class='mat-icon mes-icon material-icons ic_mw_addbutton']")
