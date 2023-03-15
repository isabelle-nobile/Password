import random
import string
from hashlib import sha256
import json
import os
import random

path_to_json = "./passwords_list.json"


def load_password_history_from_json():
    """Charge le fichier json"""
    if not os.path.isfile(path_to_json):
        return []

    with open(path_to_json, "r") as handler:
        info = json.load(handler)

    return info["passwords"]


def save_json_password(password):
    """Sauvegarde le mot de passe haché dans un fichier json"""
    if not os.path.exists(path_to_json):
        with open(path_to_json, "w") as handler:
            json.dump({"passwords": []}, handler)

    with open(path_to_json, "r") as handler:
        info = json.load(handler)

    hashed_password = hash_password(password)
    passwords = info["passwords"]
    passwords.append(hashed_password)

    with open(path_to_json, "w") as handler:
        json.dump(info, handler, indent=4)

    print("Le mot de passe '{}' est sauvegardé dans un fichier JSON.".format(password))


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


def is_password_used(password_history, password):
    """ Vérifie si le mot de passe a déjà été utilisé dans l'historique """
    hashed_password = hash_password(password)
    for hashed_password_history in password_history:
        if hashed_password == hashed_password_history:
            return True
    return False


def main():
    password_history = load_password_history_from_json()
    while True:
        password = generate_password()
        encode_p = hash_password(password)
        if is_password_used(password_history, encode_p) > 0:
            print(
                "\nVous avez déjà utilisé ce mot de passe, veuillez en choisir un autre.")
        else:
            save_json_password(encode_p)
            print("\nLe mot de passe n'a jamais été utilisé.")
            break

