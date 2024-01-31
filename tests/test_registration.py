import pytest

from pages.registration_page import RegistrationPage
from tests.base_test import BaseTest
from utils.test_data import TestData


class TestRegistration(BaseTest):
    @pytest.mark.reg_test()
    def test_registration_form(self):
        registration_page = RegistrationPage(self.driver)

        registration_page.set_first_name(TestData.first_name, 2)
        registration_page.set_last_name(TestData.second_name, 2)

        registration_page.set_email(TestData.email, 2)

        registration_page.set_gender(TestData.gender, 2)

        registration_page.set_mobile_number(TestData.mobile_number, 2)

        registration_page.set_date_of_birth(TestData.month_index, TestData.year_index, TestData.day_index, 1)

        registration_page.set_subject(TestData.subject, 2)

        registration_page.set_hobby(TestData.hobby, 2)

        registration_page.set_picture(TestData.image_path, 2)

        registration_page.scroll_page_to_bottom(2)

        registration_page.set_address(TestData.address, 2)

        registration_page.set_state(TestData.state, 2)
        registration_page.set_city(TestData.city, 2)

        registration_modal = registration_page.submit_registration(2)

        registration_modal.check_name(TestData.first_name + ' ' + TestData.second_name)
        registration_modal.check_email(TestData.email)
        registration_modal.check_gender(TestData.gender)
        registration_modal.check_mobile(TestData.mobile_number)
        registration_modal.check_birth_date(TestData.date)
        registration_modal.check_subject(TestData.subject)
        registration_modal.check_hobby(TestData.hobby)
        registration_modal.check_picture_name(TestData.image_name)
        registration_modal.check_address(TestData.address)
        registration_modal.check_state_and_city(TestData.state + ' ' + TestData.city)
