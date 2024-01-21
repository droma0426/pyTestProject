from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

OUTPUT_PATH = "C:\\Users\\droma\\Desktop\\Code\\tasks\\sillicium\\pytestProject\\output\\"
FIRST_NAME = "autotest1"
LAST_NAME = "autotest2"
EMAIL = "some@email.com"
MOBILE = "0123456789"


def test_registration_form():
    # solving certificate problem
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # opening page
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://demoqa.com/automation-practice-form")

    # filling name
    driver.find_element(By.ID, "firstName").send_keys(FIRST_NAME)
    driver.find_element(By.ID, "lastName").send_keys(LAST_NAME)

    # filling email
    driver.find_element(By.XPATH, '//div[@id="userEmail-wrapper"]//input').send_keys(EMAIL)

    # selecting gender
    driver.find_element(By.CSS_SELECTOR, 'label[for="gender-radio-1"]').click()

    # filling mobile
    driver.find_element(By.XPATH, '//div[@id="userNumber-wrapper"]//input[@id="userNumber"]').send_keys(MOBILE)

    # driver.find_element(By.ID, 'dateOfBirthInput').click()
    #
    # select_element = driver.find_element(By.XPATH,
    #                                      "//div[@class='react-datepicker']//div[@class='react-datepicker__header']//select")
    #
    # print(select_element)
    #
    # select = Select(select_element)
    # select.select_by_index(3)

    #
    # select = Select()
    # select.select_by_value("January")

    driver.save_screenshot(OUTPUT_PATH + 'test_registration_form.png')
