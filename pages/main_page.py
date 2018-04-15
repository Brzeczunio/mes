from selenium import webdriver
from base.base import Page
from locators.main_page_locators import MainPageLocatars
from locators.progress_action_locators import ProgressActionLocators
from locators.screen_blockers_locators import ScreenBlokersLocators

class MainPage(Page):
    def click_menu_button(self):
        self.find_element(MainPageLocatars.MENU_BUTTON).click()

    def get_operator_info(self):
        return self.find_element(MainPageLocatars.OPERATOR_INFO).text

    def click_logout_button(self):
        self.find_element(ScreenBlokersLocators.SCREEN_BLOKER)
        self.find_element(MainPageLocatars.LOGOUT_BUTTON).click()

    def click_action_button(self):
        self.invisibility_element(ProgressActionLocators.PROGRESS_SPINNER)
        self.invisibility_element(ScreenBlokersLocators.SCREEN_BLOKER)
        self.find_element(MainPageLocatars.ACTION_BUTTON).click()

    def click_action_add_production_button(self):
        self.invisibility_element(ProgressActionLocators.PROGRESS_SPINNER)
        self.invisibility_element(ScreenBlokersLocators.SCREEN_BLOKER)
        self.find_element(MainPageLocatars.ADD_PRODUCTION_BUTTON).click()
        self.invisibility_element(ProgressActionLocators.PROGRESS_SPINNER)
        self.invisibility_element(MainPageLocatars.ADD_PRODUCTION_BUTTON)

    def get_success_message(self):
        return self.find_element(MainPageLocatars.SUCCESS_MESSAGE).text
