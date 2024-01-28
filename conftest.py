import pytest
from selenium import webdriver

from utils.test_data import TestData


@pytest.fixture()
def init_driver(request):
    # solving certificate problem
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # opening page
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    driver.maximize_window()
    driver.get(TestData.url)
    yield
    driver.close()
