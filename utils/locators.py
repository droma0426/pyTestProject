from selenium.webdriver.common.by import By


class Locators:
    first_name_field = By.CSS_SELECTOR, 'input[placeholder="First Name"]'
    last_name_field = By.ID, "lastName"

    email_field = By.XPATH, '//div[@id="userEmail-wrapper"]//input'

    @staticmethod
    def get_gender_field_selector(gender='Male'):
        return By.XPATH, f'//div[@id="genterWrapper"]//input[@value="{gender}"]/ancestor::div[1]//label'

    mobile_field = By.XPATH, '//div[@id="userNumber-wrapper"]//input[@id="userNumber"]'

    date_dialog_field = By.ID, "dateOfBirthInput"

    month_field = By.XPATH, ("//div[@class='react-datepicker']//div[@class='react-datepicker__header']//select["
                             "@class='react-datepicker__month-select']")

    year_field = By.XPATH, ("//div[@class='react-datepicker']//div[@class='react-datepicker__header']//select["
                            "@class='react-datepicker__year-select']")

    @staticmethod
    def get_day_field_selector(day=22):
        return By.XPATH, (f'//div[@class="react-datepicker"]//div[@class="react-datepicker__month"]//div['
                          f'@class="react-datepicker__week"]//div[text()="{day}"]')

    subjects_field = By.ID, 'subjectsInput'

    @staticmethod
    def get_hobby_field_selector(hobby='Sports'):
        return By.XPATH, f'//div[@id="hobbiesWrapper"]//label[text()="{hobby}"]'

    picture_field = By.ID, 'uploadPicture'

    address_field = By.ID, 'currentAddress'

    state_field_field = By.XPATH, '//div[@id="state"]//div[contains(@class, "indicatorContainer")]'

    @staticmethod
    def get_state_option_field_selector(state='NCR'):
        return By.XPATH, f'//div[@id="stateCity-wrapper"]//div[contains(@id,"react-select-3") and text()="{state}"]'

    city_field_field = By.XPATH, '//div[@id="city"]//div[contains(@class, "indicatorContainer")]'

    @staticmethod
    def get_city_option_field_selector(city='Delhi'):
        return By.XPATH, f'//div[@id="stateCity-wrapper"]//div[contains(@id,"react-select-4") and text()="{city}"]'

    submit_button_field = By.XPATH, '//button[@id="submit"]/ancestor::div[1]'

    modal_title_field = By.XPATH, '//div[@class="modal-content"]//div[@id="example-modal-sizes-title-lg"]'

    modal_student_name_field = By.XPATH, '//table//tbody//tr[1]//td[2]'

    modal_student_email_field = By.XPATH, '//table//tbody//tr[2]//td[2]'

    modal_gender_field = By.XPATH, '//table//tbody//tr[3]//td[2]'

    modal_mobile_field = By.XPATH, '//table//tbody//tr[4]//td[2]'

    modal_date_of_birth_field = By.XPATH, '//table//tbody//tr[5]//td[2]'

    modal_subjects_field = By.XPATH, '//table//tbody//tr[6]//td[2]'

    modal_hobbies_field = By.XPATH, '//table//tbody//tr[7]//td[2]'

    modal_picture_field = By.XPATH, '//table//tbody//tr[8]//td[2]'

    modal_address_field = By.XPATH, '//table//tbody//tr[9]//td[2]'

    modal_state_and_city_field = By.XPATH, '//table//tbody//tr[10]//td[2]'
