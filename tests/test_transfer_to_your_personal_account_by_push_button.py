from selenium.webdriver.common.by import By
from conftest import driver, login


def test_transfer_to_your_personal_account_by_push_button(driver, login):
    actual_result = driver.find_element(By.XPATH, './/h2[text()= "Вход"]')
    assert actual_result.text == 'Вход'
