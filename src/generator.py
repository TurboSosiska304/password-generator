import random
import string
import hashlib

def generate_password(length, use_uppercase, use_digits, use_specials):
    chars = list(string.ascii_lowercase)

    if use_uppercase:
        chars += list(string.ascii_uppercase)
    if use_digits:
        chars += list(string.digits)
    if use_specials:
        chars += list("!@#$%^&*()-_=+[]{};:,.<>?/")

    if not chars:
        raise ValueError("Невозможно создать пароль — нет выбранных символов.")

    return ''.join(random.choice(chars) for _ in range(length))

def generate_password_from_master(master, index, length, use_uppercase, use_digits, use_specials):
    chars = list(string.ascii_lowercase)
    if use_uppercase:
        chars += list(string.ascii_uppercase)
    if use_digits:
        chars += list(string.digits)
    if use_specials:
        chars += list("!@#$%^&*()-_=+[]{};:,.<>?/")

    if not chars:
        raise ValueError("Нет символов для генерации!")

    hash_input = f"{master}_{index}".encode('utf-8')
    hashed = hashlib.sha256(hash_input).hexdigest()

    password = ''
    for i in range(length):
        chunk = hashed[i*2:i*2+2]
        idx = int(chunk, 16) % len(chars)
        password += chars[idx]

    return password
