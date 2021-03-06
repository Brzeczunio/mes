from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page(object):
    def __init__(self, driver, wait=60, base_url="http://192.168.1.63:777/"):
        self.__SCREEN_BLOKER = (By.XPATH, "//div[@class='ui-blockui ui-widget-overlay ui-blockui-document']")
        self.__PROGRESS_SPINNER = (By.XPATH, "//mat-progress-spinner[@class='mat-progress-spinner mat-primary mat-progress-spinner-indeterminate-animation']")
        self.base_url = base_url
        self.driver = driver
        self.wait = WebDriverWait(self.driver, wait)

    def wait_for_unblock_ui(self):
        self.wait.until(EC.invisibility_of_element_located(self.__PROGRESS_SPINNER))
        self.wait.until(EC.invisibility_of_element_located(self.__SCREEN_BLOKER))

    def invisibility_element(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def get_text_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def set_text_element(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def user_click_element(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))
        element = self.wait.until(EC.visibility_of_element_located(locator))
        action = ActionChains(self.driver).move_to_element(element)
        self.wait.until(EC.element_to_be_clickable(locator))
        action.click()
        action.perform()

    def scroll_to_element(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        scroll = ActionChains(self.driver).move_to_element(element)
        scroll.perform()
        return element

    def find_element_force_click(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].click()", element)

    class BUTTON(object):
        pass

    class INPUT(object):
        pass

    class MESSAGE(object):
        pass

    class BREADCRUMB(object):
        pass

    class INFO(object):
        pass
