import time
from selenium.webdriver.common.by import By
from conftest import driver, main_page


def test_transition_to_the_filling_section(driver, main_page):
    filling_element = driver.find_element(By.XPATH, './/span[contains(text(), "Начинки")]/parent::div')
    filling_element.click()
    filling_div_class = filling_element.get_attribute('class')
    assert filling_div_class == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
    time.sleep(3)
