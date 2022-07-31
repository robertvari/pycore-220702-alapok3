import os


class BattleOfClasses:
    def __init__(self):
        self.clear_screen()
        self._intro()

    @staticmethod
    def _intro():
        print("-"*50, "Battle Of Classes", "-"*50)

    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def _exit_game():
        print("Have a nice day traveller!")
        exit()


BattleOfClasses()
