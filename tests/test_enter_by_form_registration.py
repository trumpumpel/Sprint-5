from selenium.webdriver.common.by import By
from conftest import driver, register_page


def test_enter_by_form_registration(driver, register_page):
    actual_result = driver.find_element(By.XPATH, './/h2[text()= "Вход"]')
    assert actual_result.text == 'Вход'
