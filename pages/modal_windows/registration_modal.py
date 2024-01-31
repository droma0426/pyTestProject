import allure

from pages.modal_windows.base_modal import BaseModal
from utils.locators import Locators


class RegistrationModal(BaseModal):
    def __init__(self, driver):
        self.locate = Locators
        super().__init__(driver)

    @allure.step("Checking modal window title")
    def check_modal_title(self, expected_title):
        title = self.get_text(self.locate.modal_title_field)
        assert title == expected_title, "Title is not equal to expected title"

    @allure.step("Checking student name")
    def check_name(self, expected_name):
        name = self.get_text(self.locate.modal_student_name_field)
        assert name == expected_name, "Name is not equal to expected name"

    @allure.step("Checking student email")
    def check_email(self, expected_email):
        email = self.get_text(self.locate.modal_student_email_field)
        assert email == expected_email, "Email is not equal to expected email address"

    @allure.step("Checking student gender")
    def check_gender(self, expected_gender):
        gender = self.get_text(self.locate.modal_gender_field)
        assert gender == expected_gender, "Gender is not equal to expected gender"

    @allure.step("Checking student mobile number")
    def check_mobile(self, expected_mobile):
        mobile = self.get_text(self.locate.modal_mobile_field)
        assert mobile == expected_mobile, "Mobile is not equal to expected mobile"

    @allure.step("Checking student birth date")
    def check_birth_date(self, expected_date):
        date = self.get_text(self.locate.modal_date_of_birth_field)
        assert date == expected_date, "Date is not equal to expected date"

    @allure.step("Checking student subject")
    def check_subject(self, expected_subject):
        subject = self.get_text(self.locate.modal_subjects_field)
        assert subject == expected_subject, "Subject is not equal to expected subject"

    @allure.step("Checking student hobby")
    def check_hobby(self, expected_hobby):
        hobby = self.get_text(self.locate.modal_hobbies_field)
        assert hobby == expected_hobby, "Hobby is not equal to expected one"

    @allure.step("Checking student image name")
    def check_picture_name(self, expected_picture_name):
        picture_name = self.get_text(self.locate.modal_picture_field)
        assert picture_name == expected_picture_name, "Picture name is not equal to expected picture name"

    @allure.step("Checking student address")
    def check_address(self, expected_address):
        address = self.get_text(self.locate.modal_address_field)
        assert address == expected_address, "Address is not equal to expected address"

    @allure.step("Checking student state and city")
    def check_state_and_city(self, expected_state_and_city):
        state_and_city = self.get_text(self.locate.modal_state_and_city_field)
        assert state_and_city == expected_state_and_city, "State and city are not equal to expected ones"
