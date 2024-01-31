import os


class TestData:
    url = 'https://demoqa.com/automation-practice-form'
    modal_title = 'Thanks for submitting the form'
    email = "some@email.com"
    mobile_number = "0123456789"
    first_name = "autotest1"
    second_name = "autotest2"
    month_index = 3
    year_index = 120
    day_index = 22
    subject = 'English'
    hobby = 'Sports'
    image_path = os.path.abspath('resources/test_image.png')
    image_name = 'test_image.png'
    address = 'some address'
    gender = 'Male'
    date = '22 April,2020'
    state = 'NCR'
    city = 'Delhi'
    output_path = os.path.abspath('output/test_registration_form.png')