from selenium.webdriver.common.by import By
from conftest import driver, forgot_password_page


def test_enter_by_forgot_password_page(driver, forgot_password_page):
    actual_result = driver.find_element(By.XPATH, './/h2[text()= "Вход"]')
    assert actual_result.text == 'Вход'
