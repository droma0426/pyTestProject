import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

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
    time.sleep(2)

    # filling email
    driver.find_element(By.XPATH, '//div[@id="userEmail-wrapper"]//input').send_keys(EMAIL)
    time.sleep(2)

    # selecting gender
    driver.find_element(By.CSS_SELECTOR, 'label[for="gender-radio-1"]').click()
    time.sleep(2)

    # filling mobile
    driver.find_element(By.XPATH, '//div[@id="userNumber-wrapper"]//input[@id="userNumber"]').send_keys(MOBILE)
    time.sleep(2)

    # filling date
    driver.find_element(By.ID, 'dateOfBirthInput').click()

    # selecting month
    select_element_month = driver.find_element(By.XPATH,
                                               "//div[@class='react-datepicker']"
                                               "//div[@class='react-datepicker__header']"
                                               "//select[@class='react-datepicker__month-select']")

    select_month = Select(select_element_month)
    select_month.select_by_index(3)
    time.sleep(1)

    # selecting year
    select_element_year = driver.find_element(By.XPATH,
                                              "//div[@class='react-datepicker']"
                                              "//div[@class='react-datepicker__header']"
                                              "//select[@class='react-datepicker__year-select']")

    select_year = Select(select_element_year)
    select_year.select_by_index(120)
    time.sleep(1)

    # selecting day
    driver.find_element(By.XPATH, '//div[@class="react-datepicker"]'
                                  '//div[@class="react-datepicker__month"]'
                                  '//div[@class="react-datepicker__week"]'
                                  '//div[text()="22"]').click()
    time.sleep(1)

    # selecting subject
    subject_field = driver.find_element(By.ID, 'subjectsInput')
    subject_field.send_keys('English')
    subject_field.send_keys(Keys.ENTER)
    time.sleep(2)

    # selecting hobby
    hobby_selector = driver.find_element(By.XPATH, '//div[@id="hobbiesWrapper"]//label[text()="Sports"]')
    hobby_selector.click()
    time.sleep(2)

    # selecting picture
    driver.find_element(By.ID, 'uploadPicture').send_keys(os.path.abspath('resources/test_image.png'))
    time.sleep(2)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # filling address
    driver.find_element(By.ID, 'currentAddress').send_keys('filling text')
    time.sleep(2)

    # selecting state
    driver.find_element(By.XPATH, '//div[@id="state"]//div[contains(@class, "indicatorContainer")]').click()

    state_option = driver.find_element(By.ID, 'react-select-3-option-0')
    state_option.click()
    time.sleep(2)

    # selecting city
    driver.find_element(By.XPATH, '//div[@id="city"]//div[contains(@class, "indicatorContainer")]').click()

    city_option = driver.find_element(By.ID, 'react-select-4-option-0')
    city_option.click()

    time.sleep(2)

    # clicking submit button
    submit_button = driver.find_element(By.XPATH, '//button[@id="submit"]/ancestor::div[1]')
    submit_button.submit()

    time.sleep(2)

    # checking appearance of modal
    modal_title = driver.find_element(By.XPATH, '//div[@class="modal-content"]'
                                                '//div[@id="example-modal-sizes-title-lg"]').text

    assert modal_title == 'Thanks for submitting the form'

    # checking values
    student_name = driver.find_element(By.XPATH, '//table//tbody//tr[1]//td[2]').text
    assert student_name == 'autotest1 autotest2'

    student_email = driver.find_element(By.XPATH, '//table//tbody//tr[2]//td[2]').text
    assert student_email == 'some@email.com'

    gender = driver.find_element(By.XPATH, '//table//tbody//tr[3]//td[2]').text
    assert gender == 'Male'

    mobile = driver.find_element(By.XPATH, '//table//tbody//tr[4]//td[2]').text
    assert mobile == '0123456789'

    date_of_birth = driver.find_element(By.XPATH, '//table//tbody//tr[5]//td[2]').text
    assert date_of_birth == '22 April,2020'

    subjects = driver.find_element(By.XPATH, '//table//tbody//tr[6]//td[2]').text
    assert subjects == 'English'

    hobbies = driver.find_element(By.XPATH, '//table//tbody//tr[7]//td[2]').text
    assert hobbies == 'Sports'

    picture = driver.find_element(By.XPATH, '//table//tbody//tr[8]//td[2]').text
    assert picture == 'test_image.png'

    address = driver.find_element(By.XPATH, '//table//tbody//tr[9]//td[2]').text
    assert address == 'filling text'

    state_and_city = driver.find_element(By.XPATH, '//table//tbody//tr[10]//td[2]').text
    assert state_and_city == 'NCR Delhi'

    # saving screenshot
    driver.save_screenshot(os.path.abspath('output/test_registration_form.png'))

