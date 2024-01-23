from selene import browser, have, be
from selene.core import command
import os

def test_demoqa_form():
    browser.open('/')
    browser.element('#firstName').should(be.blank).send_keys('Ivan')
    browser.element('#lastName').should(be.blank).send_keys('Ivanov')
    browser.element('#userEmail').should(be.blank).send_keys('Ivanov@test.com')
    browser.element('#gender-radio-1').double_click()
    browser.element('#userNumber').should(be.blank).send_keys('89999876543')
    browser.element('#dateOfBirthInput').perform(command.js.set_value('10 Jan 1980'))
    browser.element('#uploadPicture').send_keys(os.path.abspath('picture.jpg'))
    browser.element("[class='custom-control custom-checkbox custom-control-inline']").click()
    browser.element('#subjectsInput').type('Physics').press_enter()
    browser.element('#currentAddress').send_keys('111999, St Hall avenue 34')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').submit()
    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.element('#closeLargeModal').double_click()
