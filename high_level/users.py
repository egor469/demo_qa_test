from dataclasses import dataclass

@dataclass
class User:
    firstName: str
    lastName: str
    email: str
    gender: str
    mobile: str
    birth_day: str
    birth_month: str
    birth_year: str
    subjects: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str
    text_birth_month: str


test_user = User(firstName='Ivan', lastName='Klochko', email='Klochko.i@yandex.ru', gender='Male', mobile='9098087766',
                 text_birth_month='March',
                 birth_day='09', birth_month='2', birth_year='1990', subjects='Math', hobby='Sports',
                 picture='img.jpg', address='Test, 3/14', state='NCR', city='Delhi')