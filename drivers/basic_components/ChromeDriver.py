#!/usr/bin/env python

from time import sleep
from time import time
from pyperclip import paste

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

mac_chromedriver_path = "resourses/chromedriver_mac"
linux_chromedriver_path = "resourses/chromedriver_linux"


class ChromeDriver(WebDriver):
    def __init__(self):
        options = Options()
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-infobars")
        super(ChromeDriver, self).__init__(executable_path=linux_chromedriver_path, chrome_options=options)

        self.implicitly_wait(2)
        self.set_window_size(1920, 1080)
        self.set_page_load_timeout(60)

    def wait_for_page_title(self, title):
        return WebDriverWait(self, 5).until(EC.title_contains(title))

    @staticmethod
    def get_clipboard():
        text = paste()
        return text

    @staticmethod
    def wait_until(condition, params=(), timeout=20, sleep_interval=0.5):
        start = time()
        while time() - start < timeout:
            try:
                res = condition(*params)
                if res:
                    return res
            except Exception:
                pass
            sleep(sleep_interval)
        return False
