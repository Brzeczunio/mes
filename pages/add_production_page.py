from selenium import webdriver
from base.base import Page
from locators.add_production_page_locators import AddProductionPageLocators
from locators.progress_action_locators import ProgressActionLocators

class AddProductionPage(Page):
    def enter_production(self, production):
        self.find_element(AddProductionPageLocators.ADD_PRODUCTION_INPUT).send_keys(production)

    def click_add_production_button(self):
        self.find_element_force_click(AddProductionPageLocators.ADD_PRODUCTION_BUTTON)
        self.invisibility_element(ProgressActionLocators.PROGRESS_SPINNER)
