import time
from selenium.webdriver.common.by import By
from conftest import driver, main_page


def test_transition_to_the_bread_section(driver, main_page):
    sauces_element = driver.find_element(By.XPATH, './/span[contains(text(), "Соусы")]/parent::div')
    sauces_element.click()
    bread_element = driver.find_element(By.XPATH, './/span[contains(text(), "Булки")]/parent::div')
    bread_element.click()
    bread_div_class = bread_element.get_attribute('class')
    assert bread_div_class == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
    time.sleep(3)
