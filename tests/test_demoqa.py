from selene.support.shared import browser
from selene import have, be
import os


def test_registration_form():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').should(be.blank).type('Chev')
    browser.element('#lastName').should(be.blank).type('Chelios')
    browser.element('#userEmail').should(be.blank).type('test_090@gmail.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type(7298965483)
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="11"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1980"]').click()
    browser.element('.react-datepicker__day--008').click()
    browser.element('#subjectsInput').type('Accounting').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element("#uploadPicture").set_value(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'picture_test/sampleFile.jpeg')))
    browser.element('#currentAddress').type('Moscow')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').press_enter()


def test_conformity():
    browser.all('.table tr td ~td').should(
        have.texts('Chev Chelios', 'test_090@gmail.com', 'Male', '7298965483', '08 December,1980', 'Accounting',
                   'Sports', 'sampleFile.jpeg', 'Moscow', 'NCR Delhi'))
