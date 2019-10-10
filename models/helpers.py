from string import ascii_letters
from string import digits
from random import choice
from hashlib import md5


def get_password_hash(password):
    hashed = md5(password.encode('utf-8'))
    return hashed.digest()


def generate_random_token(characters=ascii_letters+digits, length=8):
    return ''.join([choice(characters) for _ in range(length)])
