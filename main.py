from hashlib import sha256
import json
import re
import os

path_to_json = "./passwords_list.json"


def save_json_password(password):
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


def check_password(password):
    if len(password) < 8:
        print("Votre mot de passe doit au moins contenir 8 caractères.")
        main()
    elif re.search('[0-9]',password) is None:
        print("Votre mot de passe doit au moins contenir un nombre.")
        main()
    elif re.search('[A-Z]',password) is None:
        print("Votre mot de passe doit au moins contenir une lettre majuscule.")
        main()
    elif re.search('[!@#$%^&*]',password) is None:
        print("Votre mot de passe doit au moins contenir un caractère spécial (!, @, #, $, %, ^, &, *).")
        main()
    else:
        print("Votre mot de passe est valide !")
    return password


def hash_password(password):
    return sha256(password.encode('utf-8')).hexdigest() 

def main():
    password = input('Veuillez entrer votre mot de passe:')
    check_password(password)
    encode_p = hash_password(password)
    # return print(encode_p)
    return save_json_password(encode_p)


if __name__ == "__main__":
    main()

