from conftest import driver, register, register_short_password
from locators import enter_heading, invalid_password

from selenium.webdriver.common.by import By


def test_registration(driver, register):
    actual_result = driver.find_element(By.XPATH, enter_heading)
    assert actual_result.text == 'Вход'


def test_registration_short_password(driver, register_short_password):
    actual_result = driver.find_element(By.CSS_SELECTOR, invalid_password)
    assert actual_result.text == 'Некорректный пароль'
