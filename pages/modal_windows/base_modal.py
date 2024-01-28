class BaseModal:
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(by=locator[0], value=locator[1])

    def get_text(self, *locator):
        return self.find(*locator).text
