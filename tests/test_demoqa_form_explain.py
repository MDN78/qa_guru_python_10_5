from selene import browser, have, be, by
import os
import time

# Стили комментариев:
# 1) AAA - Arrange, Act, Assert
# 2) BDD - Given, When, Then

def test_student_registration_form():
    '''
    Разбор занятия. Разобраны селекторы и более качественное оформление кода.
    Подход к выбору селекторов - чтобы они так же помогали понять что ищем и над чем работает строчка
    '''
    browser.open('/automation-practice-form')

    # WHEN
    browser.element('#firstName').should(be.blank).send_keys('Ivan')
    browser.element('#lastName').should(be.blank).send_keys('Ivanov')
    browser.element('#userEmail').should(be.blank).send_keys('Ivanov@test.com')
    # Так когда более понятен - вводим переменную и селекторы помогают понять что ищем
    '''
    male_radio = browser.element('[name=gender][value=Male]')
    male_radio.double_click()
    
    Другой вариант - тк тут есть перекрытие элемента - тогда не нужен двойной клик:  
    male_radio = browser.element('[name=gender][value=Male]+label')
    male_radio.click()
    
    Так записать правильней и короче - мы понимаем что есть кнопка Гендер - там несколько значений
    И среди этих значений выбираем именно Male. Так же разделяя селекторы - при падении и ошибке - проще понять на каком селекторе
    споткнулся код. Но при разбивке селекторов не получится дописать сиблинга только через Xpath
    те кликаем на следующий идущий элемент:
    male_radio = browser.all('[name=gender]').element_by(have.value('Male')).element('./following-sibling::*')
    male_radio.click()
    '''
    # Так же можем кликнуть по иву выше - это проще не надо писать xpath - указать '..' - это значит на элемент выше
    male_radio = browser.all('[name=gender]').element_by(have.value('Male')).element('..')
    male_radio.click()
    browser.element('#userNumber').should(be.blank).send_keys('1234567890')

    time .sleep(3)
