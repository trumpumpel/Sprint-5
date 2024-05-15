import random
import string


def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


r_name = (random_char(9))
r_email = (random_char(7) + "@yah.com")
r_password = (random_char(6))
cor_name = 'Zemdan'
cor_email = '1234@ya.com'
cor_password = '123ddd'
un_password = '1'
URL = 'https://stellarburgers.nomoreparties.site/'
