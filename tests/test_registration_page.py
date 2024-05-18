from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LocatorsLand
from data import URL
from helpers import r_name, r_email, r_password


class TestRegistrationPage:

    def test_register(self, driver):
        driver.get(f'{URL}/register')

        name_element = driver.find_element(*LocatorsLand.NAME_REG)
        name_element.send_keys(r_name)

        email_element = driver.find_element(*LocatorsLand.EMAIL_REG)
        email_element.send_keys(r_email)

        password_element = driver.find_element(*LocatorsLand.PASSWORD_REG)
        password_element.send_keys(r_password)

        reg_button = driver.find_element(*LocatorsLand.REG_BUTTON)
        reg_button.click()

        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(LocatorsLand.ENTER_HEADING))

        actual_result = driver.find_element(*LocatorsLand.ENTER_HEADING)
        assert actual_result.text == 'Вход'

    def test_register_wrong_password(self, driver):
        driver.get(f'{URL}/register')

        name_element = driver.find_element(*LocatorsLand.NAME_REG)
        name_element.send_keys('Zoeman')

        email_element = driver.find_element(*LocatorsLand.EMAIL_REG)
        email_element.send_keys('12388ff@ya.com')

        password_element = driver.find_element(*LocatorsLand.PASSWORD_REG)
        password_element.send_keys('1235ddd')

        reg_button = driver.find_element(*LocatorsLand.REG_BUTTON)
        reg_button.click()

        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(
            LocatorsLand.EXISTS_PASSWORD))

        actual_result = driver.find_element(*LocatorsLand.EXISTS_PASSWORD)
        assert actual_result.text == 'Такой пользователь уже существует'

    def test_register_wrong_name(self, driver):
        driver.get(f'{URL}/register')

        name_element = driver.find_element(*LocatorsLand.NAME_REG)
        name_element.send_keys('')

        email_element = driver.find_element(*LocatorsLand.EMAIL_REG)
        email_element.send_keys('12388ff@ya.com')

        password_element = driver.find_element(*LocatorsLand.PASSWORD_REG)
        password_element.send_keys('1235ddd')

        reg_button = driver.find_element(*LocatorsLand.REG_BUTTON)
        reg_button.click()

        current_url = driver.current_url
        assert driver.current_url == f'{URL}/register'

    def test_register_invalid_password(self, driver):
        driver.get(f'{URL}/register')

        name_element = driver.find_element(*LocatorsLand.NAME_REG)
        name_element.send_keys('Zoeman')

        email_element = driver.find_element(*LocatorsLand.EMAIL_REG)
        email_element.send_keys('12388ff@ya.com')

        password_element = driver.find_element(*LocatorsLand.PASSWORD_REG)
        password_element.send_keys('12')

        reg_button = driver.find_element(*LocatorsLand.REG_BUTTON)
        reg_button.click()

        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(
                LocatorsLand.INVALID_PASSWORD))

        actual_result = driver.find_element(*LocatorsLand.INVALID_PASSWORD)
        assert actual_result.text == 'Некорректный пароль'
