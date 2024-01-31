import allure

from pages.base_page import BasePage
from pages.modal_windows.registration_modal import RegistrationModal
from utils.locators import Locators


class RegistrationPage(BasePage):
    def __init__(self, driver):
        self.locate = Locators
        super().__init__(driver)

    @allure.step("Filling first name")
    def set_first_name(self, first_name, timeout):
        self.set_value(self.locate.first_name_field, value=first_name, timeout=timeout)

    @allure.step("Filling last name")
    def set_last_name(self, last_name, timeout):
        self.set_value(self.locate.last_name_field, value=last_name, timeout=timeout)

    @allure.step("Filling email address")
    def set_email(self, email, timeout):
        self.set_value(self.locate.email_field, value=email, timeout=timeout)

    @allure.step("Choosing gender")
    def set_gender(self,  gender, timeout):
        self.click(self.locate.get_gender_field_selector(gender), timeout=timeout)

    @allure.step("Filling mobile number")
    def set_mobile_number(self, mobile_number, timeout):
        self.set_value(self.locate.mobile_field, value=mobile_number, timeout=timeout)

    @allure.step("Setting birth date")
    def set_date_of_birth(self, month, year, day, timeout):
        self.click(self.locate.date_dialog_field, timeout=timeout)
        self.set_date_by_index(self.locate.month_field, index=month, timeout=timeout)
        self.set_date_by_index(self.locate.year_field, index=year, timeout=timeout)
        self.click(self.locate.get_day_field_selector(day), timeout=timeout)

    @allure.step("Choosing subject")
    def set_subject(self, subject, timeout):
        self.set_value(self.locate.subjects_field, value=subject, timeout=timeout)
        self.press_enter(self.locate.subjects_field, timeout=timeout)

    @allure.step("Choosing hobby")
    def set_hobby(self, hobby, timeout):
        self.click(self.locate.get_hobby_field_selector(hobby), timeout=timeout)

    @allure.step("Uploading picture")
    def set_picture(self, picture_path, timeout):
        self.set_value(self.locate.picture_field, value=picture_path, timeout=timeout)

    @allure.step("Filling address field")
    def set_address(self, address, timeout):
        self.set_value(self.locate.address_field, value=address, timeout=timeout)

    @allure.step("Choosing state")
    def set_state(self, state, timeout):
        self.click(self.locate.state_field_field)
        self.click(self.locate.get_state_option_field_selector(state), timeout=timeout)

    @allure.step("Choosing city")
    def set_city(self, city, timeout):
        self.click(self.locate.city_field_field)
        self.click(self.locate.get_city_option_field_selector(city), timeout=timeout)

    @allure.step("Submitting registration")
    def submit_registration(self, timeout):
        self.submit(self.locate.submit_button_field, timeout=timeout)
        return RegistrationModal(self.driver)


