from selenium.webdriver.common.by import By


class BasePage:
    _BASE_URL = 'https://stellarburgers.nomoreparties.site/'

    def __init__(self, driver, path):
        self.driver = driver
        self.path = path
        self.base_url = self._BASE_URL + self.path

    def open(self):
        self.driver.get(self.base_url)

    def login(self, email, password):
        self.__switch_between_login_and_register_page('login')
        email_element = self.driver.find_element(By.CSS_SELECTOR, 'input[name="name"]')
        password_element = self.driver.find_element(By.CSS_SELECTOR, 'input[name="Пароль"]')
        email_element.send_keys(email)
        password_element.send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, 'form>button').click()

    def register(self, name, email, password):
        self.__switch_between_login_and_register_page('register')
        name_element = self.driver.find_element(By.XPATH, './/label[text()="Имя"]/../input')
        email_element = self.driver.find_element(By.XPATH, './/label[text()="Email"]/../input')
        password_element = self.driver.find_element(By.CSS_SELECTOR, 'input[name="Пароль"]')
        name_element.send_keys(name)
        email_element.send_keys(email)
        password_element.send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, 'form>button').click()

    def __switch_between_login_and_register_page(self, target_path):
        if self.path != target_path:
            self.base_url = self._BASE_URL + target_path
            self.open()

    def enter_by_button_at_main(self):
        self.driver.find_element(By.XPATH, './/button[text()= "Войти в аккаунт"]').click()

    def enter_by_personal_account(self):
        self.driver.find_element(By.XPATH, './/p[text()= "Личный кабинет"]').click()

    def enter_by_form_registration(self):
        self.driver.find_element(By.XPATH, './/a[text()= "Войти"]').click()

    def enter_by_forgot_password_page(self):
        self.driver.find_element(By.XPATH, './/a[text()= "Войти"]').click()

    def transfer_to_your_personal_account_by_push_button(self):
        self.driver.find_element(By.XPATH, './/p[text()= "Личный кабинет"]').click()

    def click_through_to_constructor(self):
        self.driver.find_element(By.XPATH, './/p[text()="Конструктор"]').click()

    def click_through_to_stellar_burgers(self):
        self.driver.find_element(By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]').click()

    def log_out_of_your_account_using_the_button_in_personal_account(self):
        self.driver.find_element(By.XPATH, './/button[text()= "Выход"]').click()

    def transition_to_the_bread_section(self):
        # self.driver.find_element(By.XPATH, './/span[text()= "Соус"]').click()
        self.driver.find_element(By.XPATH, './/span[text()= "Булки"]').click()

    def transition_to_the_sauces_section(self):
        self.driver.find_element(By.XPATH, './/span[text()= "Соус"]').click()

    def transition_to_the_filling_section(self):
        self.driver.find_element(By.XPATH, './/span[text()= "Начинки"]').click()
