import allure

from pages.modal_windows.base_modal import BaseModal
from utils.locators import Locators


class RegistrationModal(BaseModal):
    def __init__(self, driver):
        self.locate = Locators
        super().__init__(driver)

    @allure.step("Checking student name")
    def check_name(self, expected_name):
        name = self.get_text(self.locate.modal_student_name_field)
        assert name == expected_name, "Name is not correct"

    @allure.step("Checking student email")
    def check_email(self, expected_email):
        email = self.get_text(self.locate.modal_student_email_field)
        assert email == expected_email, "Email is not correct"

    @allure.step("Checking student gender")
    def check_gender(self, expected_gender):
        gender = self.get_text(self.locate.modal_gender_field)
        assert gender == expected_gender, "Gender is not correct"

    @allure.step("Checking student mobile number")
    def check_mobile(self, expected_mobile):
        mobile = self.get_text(self.locate.modal_mobile_field)
        assert mobile == expected_mobile, "Mobile is not correct"

    @allure.step("Checking student birth date")
    def check_birth_date(self, expected_date):
        date = self.get_text(self.locate.modal_date_of_birth_field)
        assert date == expected_date, "Date is not correct"

    @allure.step("Checking student subject")
    def check_subject(self, expected_subject):
        subject = self.get_text(self.locate.modal_subjects_field)
        assert subject == expected_subject, "Subject is not correct"

    @allure.step("Checking student hobby")
    def check_hobby(self, expected_hobby):
        hobby = self.get_text(self.locate.modal_hobbies_field)
        assert hobby == expected_hobby

    @allure.step("Checking student image name")
    def check_picture_name(self, expected_picture_name):
        picture_name = self.get_text(self.locate.modal_picture_field)
        assert picture_name == expected_picture_name

    @allure.step("Checking student address")
    def check_address(self, expected_address):
        address = self.get_text(self.locate.modal_address_field)
        assert address == expected_address

    @allure.step("Checking student state and city")
    def check_state_and_city(self, expected_state_and_city):
        state_and_city = self.get_text(self.locate.modal_state_and_city_field)
        assert state_and_city == expected_state_and_city
