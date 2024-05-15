from selenium.webdriver.common.by import By


class LocatorsLand:
    EMAIL_LOG = (By.CSS_SELECTOR, "//input[name='name']")  # поле ввода email в окне Логин
    PASSWORD_LOG = (By.CSS_SELECTOR, "input[name='Пароль']")  # поле ввода пароля в окне Логин
    NAME_REG = (By.XPATH, "//label[text()='Имя']/../input")  # поле ввода имени в окне Регистрации
    EMAIL_REG = (By.XPATH, "//label[text()='Email']/../input")  # поле ввода email в окне Регистрации
    PASSWORD_REG = (By.CSS_SELECTOR, "input[name='Пароль']")  # поле ввода пароля в окне Регистрации
    EXISTS_PASSWORD = (
        By.XPATH,
        "//p[contains(@class, 'input__error text_type_main-default')]")  # текст Такой пользователь уже существует
    ENTER = (By.XPATH, "//button[text()='Войти']")  # кнопка Вход
    REG_BUTTON = (By.XPATH, "//button[contains(@class, '33qZ0')]")
    ENTER_BY_BUTTON_AT_MAIN = (
        By.XPATH, "//button[text()='Войти в аккаунт']")  # кнопка Войти в аккаунт на главной странице
    PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")  # кнопка Личный кабинет
    ENTER_BY_PERSONAL_ACCOUNT = (
        By.XPATH, "//a[text()= 'Войти']")  # кнопка Войти в окне Регистрации и форме восстановления пароля
    ENTER_AT_PERSONAL_ACCOUNT = (
        By.XPATH, "//button[text()= 'Войти']")  # кнопка Войти в Личном кабинете
    CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")  # гиперссылка Конструктор
    STELLAR_BURGER = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # гиперссылка с логотипом
    LOGOUT_ACCOUNT = (By.XPATH, "//button[contains(@class, 'Account_button__14Yp3 ')]")  # кнопка Выход Личном кабинете
    BREAD = (By.XPATH, "//span[contains(text(), 'Булки')]/parent::div")  # кнопка Булки на главной странице
    SAUCES = (By.XPATH, "//span[contains(text(), 'Соусы')]/parent::div")  # кнопка Соус на главной странице
    FILLING = (By.XPATH, "//span[contains(text(), 'Начинки')]/parent::div")  # кнопка Начинки на главной странице
    ACTIVE_FIELD = "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"  # атрибут выделенного поля
    ENTER_HEADING = (By.XPATH, "//h2[text()= 'Вход']")  # заголовок Вход
    PROFILE = (By.XPATH, "//a[text()='Профиль']")  # заголовок Профиль
    INVALID_PASSWORD = (
        By.XPATH, "//p[contains(@class, 'input__error text_type_main-default')]")  # текст Некорректный пароль
    ACTIV_LOC = (
        By.CSS_SELECTOR, "BurgerIngredients_ingredients__menuContainer__Xu3Mo")  # локатор активности ингридиента
