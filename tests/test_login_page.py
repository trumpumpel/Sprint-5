from locators import invalid_password
from conftest import driver, login
from selenium.webdriver.common.by import By


def test_correct_login_and_pasword(driver, login):
    actual_result = driver.find_element(By.CSS_SELECTOR, invalid_password)
    assert actual_result.text == 'Некорректный пароль'
