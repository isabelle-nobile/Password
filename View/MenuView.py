class MenuView:
    """La classe qui affiche le menu principal"""

    def __init__(self):
        """Afficher les possibilités du menu principal à l'utilisateur"""

        print("\n\n ---- Password Manager ----")
        print("\n\n---- Menu principal ----\n")
        print("\nMerci d'entrer un des mots suivant: ")
        print(
            "input:                ",
            "Rentrer votre propre mot de passe",
        )
        print(
            "generate:             ",
            "Generer un mot de passe aléatoire",
        )
        print(
            "quitter:              ",
            "Quitter le programme\n",
        )
        self.command = None

    def launch_command_menu(self):
        """Lance la commande du menu choisi par l'utilisateur"""

        input_option = input("Veuillez rentrer votre option : ")

        if input_option == "input":
            self.command = "input"
        elif input_option == "generate":
            self.command = "generate"
            
        elif input_option == "quitter":
            print("\nMerci d'avoir utilisé ce programme\n")
            self.command = "quitter"
        else:
            print(
                "\nMerci de rentrer la bonne commande comme indiqué",
                "dans les propositions ci-dessous\n",
            )
            self.launch_command_menu()

        return self.command