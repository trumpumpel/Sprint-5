from conftest import driver
from locators import LocatorsLand
from data import URL


class TestSBEntrance:

    def test_enter_by_button_at_main(self, driver):
        driver.get(URL)
        enter_button = driver.find_element(*LocatorsLand.ENTER_BY_BUTTON_AT_MAIN)
        enter_button.click()
        actual_result = driver.find_element(*LocatorsLand.ENTER_HEADING)
        assert actual_result.text == 'Вход'

    def test_enter_by_forgot_password_page(self, driver):
        driver.get(f'{URL}/forgot-password')
        enter_button = driver.find_element(*LocatorsLand.ENTER_BY_PERSONAL_ACCOUNT)
        enter_button.click()
        actual_result = driver.find_element(*LocatorsLand.ENTER_HEADING)
        assert actual_result.text == 'Вход'

    def test_enter_by_form_registration(self, driver):
        driver.get(f'{URL}/register')
        enter_button = driver.find_element(*LocatorsLand.ENTER_BY_PERSONAL_ACCOUNT)
        enter_button.click()
        actual_result = driver.find_element(*LocatorsLand.ENTER_HEADING)
        assert actual_result.text == 'Вход'

    def test_enter_by_personal_account(self, driver):
        driver.get(f'{URL}/login')
        enter_button = driver.find_element(*LocatorsLand.ENTER_AT_PERSONAL_ACCOUNT)
        enter_button.click()
        actual_result = driver.find_element(*LocatorsLand.ENTER_HEADING)
        assert actual_result.text == 'Вход'
