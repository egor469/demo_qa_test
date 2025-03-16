import pytest
from selene.support.shared import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    # driver_options = webdriver.ChromeOptions()   #чтоб не открывать браузер

    yield
    browser.quit()