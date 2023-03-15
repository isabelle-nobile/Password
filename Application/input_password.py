from hashlib import sha256
from colorama import Fore, Style
import json
import re
import os

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


def check_password(password):
    """Permet de vérifier si le mot de passe possède les bonnes caractéristiques """
    if len(password) < 8:
        print(Fore.RED + "Votre mot de passe doit au moins contenir 8 caractères." + Style.RESET_ALL)
        main()
    elif re.search('[0-9]', password) is None:
        print(Fore.RED + "Votre mot de passe doit au moins contenir un nombre." + Style.RESET_ALL)
        main()
    elif re.search('[A-Z]', password) is None:
        print(Fore.RED + "Votre mot de passe doit au moins contenir une lettre majuscule." + Style.RESET_ALL)
        main()
    elif re.search('[!@#$%^&*]', password) is None:
        print(Fore.RED + "Votre mot de passe doit au moins contenir un caractère spécial (!, @, #, $, %, ^, &, *)." + Style.RESET_ALL)
        main()
    else:
        if len(password) < 12:
            print(Fore.YELLOW + "Votre mot de passe est moyen." + Style.RESET_ALL)
            print("Votre mot de passe est valide !")
        else:
            print(Fore.GREEN + "Votre mot de passe est fort !" + Style.RESET_ALL)
            print("Votre mot de passe est valide !")
        return password


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
        password = input('Veuillez entrer votre mot de passe:')
        checked_password = check_password(password)
        encode_p = hash_password(checked_password)
        if is_password_used(password_history, encode_p) > 0:
            print("\nVous avez déjà utilisé ce mot de passe, veuillez en choisir un autre.")
        else:
            save_json_password(encode_p)
            print("\nLe mot de passe n'a jamais été utilisé.")
            break

