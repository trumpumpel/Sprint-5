import pytest
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    page = BasePage(driver, "login")
    page.open()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'form>button')))
    page.login('123@ya.ru', 'ddd')


@pytest.fixture
def register(driver):
    page = BasePage(driver, "register")
    page.open()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'form>button')))
    page.register('Lipetsk', 'Alex_Orlov@ya.com', 'dDd123')


@pytest.fixture
def main_page(driver):
    page = BasePage(driver, "")
    page.open()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, '.BurgerIngredients_ingredients__menuContainer__Xu3Mo')))


@pytest.fixture
def register_page(driver):
    page = BasePage(driver, "register")
    page.open()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'form>button')))
    page.login('123@ya.ru', 'ddd')


@pytest.fixture
def forgot_password_page(driver):
    page = BasePage(driver, "forgot-password")
    page.open()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'form>button')))
    page.login('123@ya.ru', 'ddd')


@pytest.fixture
def click_through_to_constructor(driver):
    page = BasePage(driver, "login")
    page.open()
    page.click_through_to_constructor()


@pytest.fixture
def log_out_of_your_account_using_the_button_in_personal_account(driver):
    page = BasePage(driver, "account/profile")
    page.open()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'form>button')))
