import time
from conftest import driver, register
from selenium.webdriver.common.by import By


def test_register(driver, register):
    time.sleep(3)
    actual_result = driver.find_element(By.CSS_SELECTOR, '.input__error')
    assert actual_result.text == 'Такой пользователь уже существует'
