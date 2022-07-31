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

        self._fight()

    def _fight(self):
        players = [self._player, self._ai_player]
        players_sorted = sorted(players, key=lambda p: p.initiative)

        player1 = players_sorted[-1]
        player2 = players_sorted[0]

        winner = None
        while True:
            player1.attack(player2)
            if player2.dead:
                winner = player1
                break

            player2.attack(player1)
            if player1.dead:
                winner = player2
                break

        print(f"The winner is {winner.name}")

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
