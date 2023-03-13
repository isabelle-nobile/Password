import sys
from os import system, name
import View.MenuView as MenuView
import Application.generator_password as generator_password
import Application.input_password as input_password

class ApplicationCtrl:
    """La classe qui gère le menu principale"""

    def start(self):
        """Lance l'application pour demander une action sur le menu principal"""
        self.command = MenuView.MenuView()
        self.menu_starting = self.command.launch_command_menu()

        if self.menu_starting == "input":
            print("")
            input_password.main()
        elif self.menu_starting == "generate":
            print("")
            generator_password.main()
        elif self.menu_starting == "supprimer":
            self.clear_terminal()
            self.start()

    def clear_terminal(self):
        """Supprimer le terminal"""
        # Pour windows
        if name == 'nt':
            _ = system('cls')
    
        # Pour mac et linux
        else:
            _ = system('clear')