from game_assets.cards import Deck
from game_assets.players import Player, AIPlayer


class Blackjack:
    def __init__(self):
        self.__intro()

        self._deck = Deck()
        self._reward = 0

        # create players
        self._players = [
            Player(),
            AIPlayer(),
            AIPlayer(),
            AIPlayer(),
        ]

        # start game
        self._start_game()

        # todo get winner
        # todo restart game
        # todo exit game

    def _start_game(self):
        self._reward = 0
        self._deck.shuffle()

        # init players hands, give bet
        for p in self._players:
            p.init_hand(self._deck)
            self._reward += p.give_bet()

        for p in self._players:
            p.draw_cards(self._deck)

        self._get_winner()

    def _get_winner(self):
        print("TODO Get Winner")

    @staticmethod
    def _exit_game():
        print("Have a nice day!")
        exit()

    @staticmethod
    def __intro():
        print("-" * 50, "BLACKJACK", "-" * 50)


Blackjack()
