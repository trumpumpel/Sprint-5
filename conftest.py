import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import enter, activ_loc
from data import r_name, r_email, r_password, cor_email, un_password, cor_name, cor_password
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
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, enter)))
    page.login(cor_email, un_password)


@pytest.fixture
def register(driver):
    page = BasePage(driver, "register")
    page.open()
    page.register(r_name, r_email, r_password)
    page.click_to_constructor()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, enter)))


@pytest.fixture
def main_page(driver):
    page = BasePage(driver, "")
    page.open()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, activ_loc)))


@pytest.fixture
def register_page(driver):
    page = BasePage(driver, "register")
    page.open()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, enter)))
    page.login(r_email, r_password)

@pytest.fixture
def register_short_password(driver):
    page = BasePage(driver, "register")
    page.open()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, enter)))
    page.login(r_email, un_password)


@pytest.fixture
def forgot_password_page(driver):
    page = BasePage(driver, "forgot-password")
    page.open()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, enter)))
    page.login(r_email, r_password)


@pytest.fixture
def click_to_constructor(driver):
    page = BasePage(driver, "login")
    page.open()
    page.click_to_constructor()


@pytest.fixture
def log_out_of_personal_account(driver):
    page = BasePage(driver, "account/profile")
    page.open()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, enter)))
