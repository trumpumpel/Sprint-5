from conftest import driver, click_to_constructor


def test_click_to_constructor(driver, click_to_constructor):
    current_url = driver.current_url
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


def test_click_to_stellar_burgers(driver, click_to_constructor):
    current_url = driver.current_url
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
