
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from drivers.basic_components import ChromeDriver

timeout = 20


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver  # type: ChromeDriver

    def wait_component_to_load(self, by_locator, time=timeout, alias=None):
        element = WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(by_locator),
            "Failed to wait for visibility of an element \'{}\'; \'{}\':\'{}\'."
                .format(alias if alias else '', by_locator[0], by_locator[1]))
        return element

    def wait_for_component_clickable(self, by_locator, time=timeout):
        return WebDriverWait(self.driver, time) \
            .until(EC.element_to_be_clickable(by_locator))
