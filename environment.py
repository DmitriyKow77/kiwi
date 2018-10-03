#!/usr/bin/env python
from drivers.basic_components.ChromeDriver import ChromeDriver


def before_scenario(context, scenario):
    context.driver = ChromeDriver()  # Init webdriver


def after_scenario(context, scenario):
    context.driver.quit()
