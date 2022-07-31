import os
from game_assets.items import ItemBase
from game_assets.characters import AIPlayer, Player


class BattleOfClasses:
    def __init__(self):
        self.clear_screen()
        self._intro()

        self._items = ItemBase.generate_item_list()

        self._ai_player = AIPlayer()
        self._player = Player()

        # give some items to players
        self._ai_player.give_items(self._items)
        self._player.give_items(self._items)

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
