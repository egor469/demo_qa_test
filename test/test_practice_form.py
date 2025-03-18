
from model.pages import RegistrationPage


def test_complete_and_submit_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.remove_banner()
    registration_page.fill_first_name('Fedor')
    registration_page.fill_last_name('Bubnov')
    registration_page.fill_email('fedor.bubnov_test@gmail.com')
    registration_page.choose_gender('Male')
    registration_page.fill_phone_number('9035033528')
    registration_page.fill_date_of__birthday(1991, 2, 18)
    registration_page.scroll_page()
    registration_page.choose_subject('History')
    registration_page.choose_hobbies("1")
    registration_page.upload_picture('foto.jpg')
    registration_page.current_adress('Test, 14/2')
    registration_page.state_select('Haryana')
    registration_page.city_select('Karnal')
    registration_page.submit_button()

    # THEN
    registration_page.assert_registered_user_info(
        'Fedor Bubnov',
        'fedor.bubnov_test@gmail.com',
        'Male',
        '9035033528',
        '18 March,1991',
        'History',
        'Sports',
        'foto.jpg',
        'Test, 14/2',
        'Haryana Karnal')