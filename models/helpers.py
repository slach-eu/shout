from hashlib import md5


def get_password_hash(password):
    hashed = md5(password.encode('utf-8'))
    return hashed.digest()
