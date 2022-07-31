class BattleOfClasses:
    def __init__(self):
        self._intro()

    @staticmethod
    def _intro():
        print("-"*100, "Battle Of Classes", "-"*100)

    @staticmethod
    def _exit_game():
        print("Have a nice day traveller!")
        exit()


BattleOfClasses()
