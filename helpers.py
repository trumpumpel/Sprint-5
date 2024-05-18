import random
import string


def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


r_name = (random_char(9))
r_email = (random_char(7) + "@yah.com")
r_password = (random_char(6))
