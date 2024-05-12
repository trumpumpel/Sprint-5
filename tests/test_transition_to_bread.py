# from selenium.webdriver.common.by import By
# from conftest import driver, main_page
# from locators import bread, sauces, active_field
#
#
# def test_transition_to_bread(driver, main_page):
#     sauces_element = driver.find_element(By.XPATH, sauces)
#     sauces_element.click()
#     bread_element = driver.find_element(By.XPATH, bread)
#     bread_element.click()
#     bread_div_class = bread_element.get_attribute('class')
#     assert bread_div_class == active_field
