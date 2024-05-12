from conftest import driver, login, forgot_password_page, register_page
from locators import enter_heading
from selenium.webdriver.common.by import By


def test_enter_by_button_at_main(driver, login):
    actual_result = driver.find_element(By.XPATH, enter_heading)
    assert actual_result.text == 'Вход'


def test_enter_by_forgot_password_page(driver, forgot_password_page):
    actual_result = driver.find_element(By.XPATH, enter_heading)
    assert actual_result.text == 'Вход'


def test_enter_by_form_registration(driver, register_page):
    actual_result = driver.find_element(By.XPATH, enter_heading)
    assert actual_result.text == 'Вход'


def test_enter_by_personal_account(driver, login):
    actual_result = driver.find_element(By.XPATH, enter_heading)
    assert actual_result.text == 'Вход'
