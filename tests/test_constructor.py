from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LocatorsLand


class TestConstructor:
    def test_click_to_bread(self, driver):
        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(
                LocatorsLand.FILLING))
        filling_element = driver.find_element(*LocatorsLand.FILLING)
        filling_element.click()

        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(
                LocatorsLand.BREAD))

        bread_element = driver.find_element(*LocatorsLand.BREAD)
        bread_element.click()
        bread_div_class = bread_element.get_attribute('class')
        assert bread_div_class == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"

    def test_click_to_sauces(self, driver):
        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(
                LocatorsLand.SAUCES))

        sauces_element = driver.find_element(*LocatorsLand.SAUCES)
        sauces_element.click()
        sauces_div_class = sauces_element.get_attribute('class')
        assert sauces_div_class == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"

    def test_click_to_filling(self, driver):
        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(
                LocatorsLand.FILLING))

        filling_element = driver.find_element(*LocatorsLand.FILLING)
        filling_element.click()
        filling_div_class = filling_element.get_attribute('class')
        assert filling_div_class == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"
