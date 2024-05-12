from conftest import driver, login
from locators import enter_heading
from selenium.webdriver.common.by import By


def test_log_out_of_personal_account(driver, login):
    actual_result = driver.find_element(By.XPATH, enter_heading)
    assert actual_result.text == 'Вход'
