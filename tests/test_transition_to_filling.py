from selenium.webdriver.common.by import By
from conftest import driver, main_page
from locators import filling, active_field


def test_transition_to_filling(driver, main_page):
    filling_element = driver.find_element(By.XPATH, filling)
    filling_element.click()
    filling_div_class = filling_element.get_attribute('class')
    assert filling_div_class == active_field
