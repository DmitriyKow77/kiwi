import time
from behave import *

from drivers.bitly_page.bitly_page import BitLyPage

from drivers.basic_components import ChromeDriver


@given("I am at bitly home page")
def step_impl(context):
    driver = context.driver  # type: ChromeDriver
    driver.get("https://bitly.com/")
    assert driver.wait_for_page_title("Bitly | URL Shortener, Custom Branded URLs, API & Link Management"), \
        "Unexpected title " + driver.title


@when('I shorten url "{}"')
def step_impl(context, url):
    context.initial_url = url
    bitly_page = BitLyPage(context.driver)

    bitly_page.shorten_input().send_keys(url)
    context.driver.wait_until(lambda i: url in i.get_attribute("value"), [bitly_page.shorten_input()], 5)
    time.sleep(1)
    bitly_page.shorten_submit_button().click()
    bitly_page.copy_button().click()


@step("I check url is shorten")
def step_impl(context):
    driver = context.driver  # type: ChromeDriver
    context.shorten_url = driver.get_clipboard()
    assert "https://bit.ly/" in context.shorten_url, "Shorten url is incorrect"
    assert len(context.shorten_url) < (15 + 8), "Shorten link is too long"

@then("I go to shorten url")
def step_impl(context):
    context.driver.get(context.shorten_url)


@step("I check opens initial url")
def step_impl(context):
    assert context.driver.current_url == context.initial_url, \
        "Expected url was {} but is {}".format(context.driver.current_url, context.initial_url)