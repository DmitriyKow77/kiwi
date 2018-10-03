from selenium.webdriver.common.by import By

from drivers.basic_components.page_base import BasePage

timeout = 5


class BitLyPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver

    def shorten_input(self):
        return self.wait_component_to_load((By.ID, "shorten_url"), timeout)

    def shorten_submit_button(self):
        return self.wait_for_component_clickable((By.ID, "shorten_btn"), timeout)

    def copy_button(self):
        return self.wait_for_component_clickable((By.ID, "copy_shortlink"), timeout)
