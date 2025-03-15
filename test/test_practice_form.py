from model.pages.registration_form import RegistrationPage


def test_complete_and_submit_form():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Fedor')
    registration_page.fill_last_name('Bubnov')
    registration_page.fill_email('fedor.bubnov_test@gmail.com')
    registration_page.choose_gender('#gender-radio-1')
    registration_page.fill_phone_number('9035033528')
    registration_page.fill_date_of_bithday(2, 1990, 18)
    registration_page.choose_subject('Eng')
    registration_page.choose_hobbies('1')
    registration_page.upload_picture('foto.jpg')
    registration_page.current_adress('Test, 14/2')
    registration_page.state_select('Haryana')
    registration_page.city_select('Karnal')
    registration_page.submit()

    # THEN
    registration_page.should_registered_user_with(
        full_name='Fedor Bubnov',
        email='fedor.bubnov_test@gmail.com',
        gender='Male',
        phone='9990006666',
        date_of_birth='03 July,1997',
        subjects='Biology, Chemistry',
        hobbies='Sports, Music',
        file_name='avatar.jpg',
        address='Sadovaya, 14',
        state='Haryana',
        city='Karnal')