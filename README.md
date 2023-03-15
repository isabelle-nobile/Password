# Password

Projet : Password - LaPlateforme

Ce projet a pour but de créer un programme en Python qui permet de vérifier si un mot de passe est sûr, de le hacher avec sha256 et de le sauvegarder dans un fichier JSON.

# Processus
## Password Input

Le programme utilise la bibliothèque hashlib pour hacher les mots de passe et la bibliothèque colorama pour colorer les messages de sortie en rouge pour les erreurs, en jaune pour les mots de passe moyens et en vert pour les mots de passe forts.

Le programme commence par définir le chemin d'accès au fichier JSON pour stocker les mots de passe hachés et créer une fonction pour charger l'historique des mots de passe à partir du fichier JSON.

## Password Generator

Ce projet a aussi une option de génèrer un mot de passe aléatoire en utilisant des lettres majuscules et minuscules, des chiffres et des caractères spéciaux. Il vérifie également que le mot de passe contient au moins deux chiffres et au moins un caractère spécial.


Dans ce programme, les fonctionnalités du menu sont :
```
input:                 Rentrer votre propre mot de passe
generate:              Generer un mot de passe aléatoire
quitter:               Quitter le programme
```

# Utilisation
## Création de l'environnement virtuel
Pour la mise en palce de l'environnement virtuel :

### Sur Windows :
Dans le Windows Powershell il faudra cloner le git.

Récupération du projet
        
        $ git clone https://github.com/isabelle-nobile/Password
Activer l'environnement virtuel
        
        $ cd Password
        $ python -m venv env 
        $ ~env\scripts\activate
Installer les modules

        $ pip install -r requirements.txt
Executer le programme

        $ python main.py

----------------------------------------------
### Sur MacOS ou Linux :
Dans le terminal, il faudra cloner le git.

Récupération du projet

        $ git clone https://github.com/isabelle-nobile/Password
Activer l'environnement virtuel

        $ cd Password
        $ python3 -m venv env 
        $ source env/bin/activate
Installer les modules

        $ pip install -r requirements.txt
Executer le programme

        $ python3 main.py