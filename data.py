import random
import string


def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


r_name = (random_char(9))
r_email = (random_char(7) + "@ya.com")
r_password = (random_char(6))
cor_name = 'Zeman'
cor_email = '123@ya.com'
cor_password = '123ddd'
un_password = '1'
