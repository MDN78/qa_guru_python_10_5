import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope='function', autouse=True)
def driver_configuration():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    # browser.open('/')


    # запуск браузера в невидимом режиме
    # browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    # driver_options = webdriver.ChromeOptions()
    # driver_options.add_argument('--headless')
    # browser.config.driver_options = driver_options

    yield
    browser.quit()
