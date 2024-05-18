import pytest

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LocatorsLand
from data import cor_email, cor_password, URL


def browser_settings():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920, 990')
    return chrome_options


@pytest.fixture
def driver():
    chrome = webdriver.Chrome(options=browser_settings())
    chrome.get(URL)

    yield chrome

    chrome.quit()


@pytest.fixture
def login(driver):
    driver.get(f'{URL}/account')

    email_element = driver.find_element(*LocatorsLand.EMAIL_REG)
    email_element.send_keys(cor_email)

    password_element = driver.find_element(*LocatorsLand.PASSWORD_REG)
    password_element.send_keys(cor_password)

    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(LocatorsLand.ENTER))

    enter_button = driver.find_element(*LocatorsLand.ENTER)
    enter_button.click()

    pa_button = driver.find_element(*LocatorsLand.PERSONAL_ACCOUNT)
    pa_button.click()
