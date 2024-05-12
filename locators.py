email_log = 'input[name="name"]'  # поле ввода email в окне Логин
password_log = 'input[name="Пароль"]'  # поле ввода пароля в окне Логин
name_reg = './/label[text()="Имя"]/../input'  # поле ввода имени в окне Регистрации
email_reg = './/label[text()="Email"]/../input'  # поле ввода email в окне Регистрации
password_reg = 'input[name="Пароль"]'  # поле ввода пароля в окне Регистрации
enter = 'form>button' # кнопка Вход
enter_by_button_at_main = './/button[text()= "Войти в аккаунт"]'  # кнопка Войти в аккаунт на главной странице
personal_account = './/p[text()= "Личный кабинет"]'  # кнопка Личный кабинет
enter_by_personal_account = './/a[text()= "Войти"]'  # кнопка Войти в окне Регистрации и форме восстановления пароля
constructor = './/p[text()="Конструктор"]'  # гиперссылка Конструктор
stellar_burger = '//div[@class="AppHeader_header__logo__2D0X2"]'  # гиперссылка с логотипом
log_out_of_your_account = './/button[text()= "Выход"]'  # кнопка Выход Личном кабинете
bread = './/span[contains(text(), "Булки")]/parent::div'  # кнопка Булки на главной странице
sauces = './/span[contains(text(), "Соусы")]/parent::div'  # кнопка Соус на главной странице
filling = './/span[contains(text(), "Начинки")]/parent::div'  # кнопка Начинки на главной странице
active_field = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect' # атрибут выделенного поля
enter_heading = './/h2[text()= "Вход"]' # заголовок Вход
invalid_password = '.input__error' # текст Некорректный пароль
activ_loc = '.BurgerIngredients_ingredients__menuContainer__Xu3Mo' # локатор активности ингридиента
