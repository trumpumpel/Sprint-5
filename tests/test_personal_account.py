from conftest import driver, login
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LocatorsLand


class TestPersonalAccount:

    def test_click_personal_account_log(self, driver, login):
        WebDriverWait(driver, 15).until(
            expected_conditions.element_to_be_clickable(
                *LocatorsLand.PERSONAL_ACCOUNT))

        btn_el = driver.find_element(*LocatorsLand.PERSONAL_ACCOUNT)
        btn_el.click()

        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(
                *LocatorsLand.PROFILE))

        actual_result = driver.find_element(*LocatorsLand.PROFILE)
        assert actual_result.text == 'Профиль'

    def test_click_personal_account_not_log(self, driver):
        WebDriverWait(driver, 15).until(
            expected_conditions.element_to_be_clickable(
                *LocatorsLand.PERSONAL_ACCOUNT))

        btn_el = driver.find_element(*LocatorsLand.PERSONAL_ACCOUNT)
        btn_el.click()

        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(
                *LocatorsLand.ENTER_HEADING))

        actual_result = driver.find_element(*LocatorsLand.ENTER_HEADING)
        assert actual_result.text == 'Вход'

    def test_log_out_of_personal_account(self, driver, login):
        WebDriverWait(driver, 15).until(
            expected_conditions.element_to_be_clickable(
                *LocatorsLand.PERSONAL_ACCOUNT))
        btn_el = driver.find_element(*LocatorsLand.PERSONAL_ACCOUNT)
        btn_el.click()
        WebDriverWait(driver, 15).until(
            expected_conditions.element_to_be_clickable(
                *LocatorsLand.LOGOUT_ACCOUNT))
        logout_button = driver.find_element(*LocatorsLand.LOGOUT_ACCOUNT)
        logout_button.click()
        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(
                *LocatorsLand.ENTER_HEADING))

        actual_result = driver.find_element(*LocatorsLand.ENTER_HEADING)
        assert actual_result.text == 'Вход'

    def test_click_to_constructor(self, driver, login):
        WebDriverWait(driver, 15).until(
            expected_conditions.element_to_be_clickable(
                *LocatorsLand.PERSONAL_ACCOUNT))

        btn_el = driver.find_element(*LocatorsLand.PERSONAL_ACCOUNT)
        btn_el.click()

        WebDriverWait(driver, 15).until(
            expected_conditions.element_to_be_clickable(
                *LocatorsLand.CONSTRUCTOR))

        con_el = driver.find_element(*LocatorsLand.CONSTRUCTOR)
        con_el.click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                *LocatorsLand.BREAD))

        bread_element = driver.find_element(*LocatorsLand.BREAD)
        bread_div_class = bread_element.get_attribute('class')
        assert bread_div_class == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"

    def test_click_to_stella_burger(self, driver, login):
        WebDriverWait(driver, 15).until(
            expected_conditions.element_to_be_clickable(
                *LocatorsLand.PERSONAL_ACCOUNT))

        btn_el = driver.find_element(*LocatorsLand.PERSONAL_ACCOUNT)
        btn_el.click()

        WebDriverWait(driver, 15).until(
            expected_conditions.element_to_be_clickable(
                *LocatorsLand.STELLAR_BURGER))

        con_el = driver.find_element(*LocatorsLand.STELLAR_BURGER)
        con_el.click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                *LocatorsLand.BREAD))

        bread_element = driver.find_element(*LocatorsLand.BREAD)
        bread_div_class = bread_element.get_attribute('class')
        assert bread_div_class == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"
