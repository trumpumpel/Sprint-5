from selenium.webdriver.common.by import By
from conftest import driver, login


def test_enter_by_personal_account(driver, login):
    actual_result = driver.find_element(By.XPATH, './/h2[text()= "Вход"]')
    assert actual_result.text == 'Вход'
