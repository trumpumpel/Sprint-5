from selenium.webdriver.common.by import By
from conftest import driver, login


def test_log_out_of_your_account_using_the_button_in_personal_account(driver,
                                                                      login):
    actual_result = driver.find_element(By.XPATH, './/h2[text()= "Вход"]')
    assert actual_result.text == 'Вход'
