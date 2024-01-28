import time

from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(by=locator[0], value=locator[1])

    def click(self, *locator, timeout=0):
        self.find(*locator).click()
        time.sleep(timeout)

    def set_value(self, *locator, value, timeout=0):
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)
        time.sleep(timeout)

    def submit(self, *locator, timeout):
        web_element = self.find(*locator)
        web_element.submit()
        time.sleep(timeout)

    def press_enter(self, *locator, timeout):
        web_element = self.find(*locator)
        web_element.send_keys(Keys.ENTER)
        time.sleep(timeout)

    def get_text(self, *locator):
        return self.find(*locator).text

    def set_date_by_index(self, *locator, index, timeout):
        select_element = self.find(*locator)
        select = Select(select_element)
        select.select_by_index(index)
        time.sleep(timeout)

    def scroll_page_to_bottom(self, timeout):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(timeout)
