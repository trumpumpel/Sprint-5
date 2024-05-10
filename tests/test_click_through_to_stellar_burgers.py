import time
from conftest import driver, click_through_to_constructor


def test_click_through_to_stellar_burgers(driver, click_through_to_constructor):
    time.sleep(3)
    current_url = driver.current_url
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
