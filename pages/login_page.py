from selenium import webdriver
from base.base import Page
from locators.login_page_locators import LoginPageLocators
from locators.progress_action_locators import ProgressActionLocators

class LoginPage(Page):
    def enter_login(self, login):
        self.find_element(LoginPageLocators.LOGIN).send_keys(login)

    def enter_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD).send_keys(password)

    def enter_terminal(self, terminal):
        self.find_element(LoginPageLocators.TERMINAL).send_keys(terminal)

    def click_login_button(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()
        self.invisibility_element(ProgressActionLocators.PROGRESS_SPINNER)

    def get_text_login_button(self):
        return self.find_element(LoginPageLocators.LOGIN_BUTTON).text
