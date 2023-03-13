import random
import string
from hashlib import sha256
import json
import os
import random

path_to_json = "./passwords_list.json"


def save_json_password(password):
    """Sauvegarde le mot de passe dans un fichier json"""
    if not os.path.exists(path_to_json):
        with open(path_to_json, "w") as handler:
            json.dump({"passwords": []}, handler)

    with open(path_to_json, "r") as handler:
        info = json.load(handler)

    passwords = info["passwords"]
    passwords.append(password)

    with open(path_to_json, "w") as handler:
        json.dump(info, handler, indent=4)

    print("Password '{}' saved to JSON file.".format(password))


def generate_password():
    """Permet de generer un mot de passe aléatoire"""
    letters = string.ascii_letters
    digits = string.digits
    special_chars = '!@#$%^&*'

    alphabet = letters + digits + special_chars

    pwd_length = 8

    while True:
        pwd = ''.join(random.choice(alphabet) for i in range(pwd_length))
        if (any(char in special_chars for char in pwd) and
                sum(char in digits for char in pwd) >= 2):
            break

    return pwd


def hash_password(password):
    """Hash avec sha256 le mot de passe et l'encode """
    return sha256(password.encode('utf-8')).hexdigest()


def main():
    password = generate_password()
    encode_p = hash_password(password)
    return save_json_password(encode_p)
