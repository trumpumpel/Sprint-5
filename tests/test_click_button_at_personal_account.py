from selenium.webdriver.common.by import By
from conftest import driver, login
from locators import enter_heading


def test_click_button_at_personal_account(driver, login):
    actual_result = driver.find_element(By.XPATH, enter_heading)
    assert actual_result.text == 'Вход'
