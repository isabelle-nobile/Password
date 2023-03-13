import string
import sys
import hashlib
import re
alpha = set(string.ascii_lowercase + string.ascii_uppercase)
digits = set(string.digits)
special_chars =  ['!', '@', '#', '$', '%', "^", "&", '*' ]

def save_password(password):
    if password == "password":
        return password
    else:
        print("Le mot de passe n'est pas valide. Merci de retenter")
       
# def check_password(password,
#                         non_alphabetic_characters=special_chars,
#                         digits_characters=digits,
#                         letters_characters=alpha):
#     if not any(character in password
#                for character in non_alphabetic_characters):
#         err_msg = ('\nLe mot de passe doit au moins contenir un carcatère spécial')
#         print(err_msg)
#         print('Mot de passe invalide')
#         ask_password()


#     if not any(character in password
#                for character in digits_characters):
#         err_msg = ('\n Le mot de passe doit au moins contenir un chiffre')
#         print(err_msg)
#         print('Mot de passe invalide')
#         ask_password()


#     if not any(character in password
#                for character in letters_characters):
#         err_msg = ('\n Le mot de passe doit au moins contenir une lettre majuscule et minucule')
#         print(err_msg)
#         print('Mot de passe invalide')
#         ask_password()


def check_password(password):
    if len(password) < 8:
        print("Votre mot de passe doit au moins contenir 8 caractères.")
        ask_password()
    elif re.search('[0-9]',password) is None:
        print("Votre mot de passe doit au moins contenir un nombre.")
        ask_password()
    elif re.search('[A-Z]',password) is None:
        print("Votre mot de passe doit au moins contenir une lettre majuscule.")
        ask_password()
    elif re.search('[!@#$%^&*]',password) is None:
        print("Votre mot de passe doit au moins contenir un caractère spécial (!, @, #, $, %, ^, &, *).")
        ask_password()
    else:
        print("Votre mot de passe est valide !")
        
    
def ask_password():
    password = input('Veuillez entrer votre mot de passe:')
    return check_password(password)


if __name__ == "__main__":
    ask_password()

