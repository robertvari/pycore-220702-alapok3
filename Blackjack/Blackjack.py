from game_assets.cards import Deck


class Blackjack:
    def __init__(self):
        self.__intro()

        self._deck = Deck()

        # todo create players
        # todo start game
        # todo get winner
        # todo restart game
        # todo exit game

    @staticmethod
    def __intro():
        print("-" * 50, "BLACKJACK", "-" * 50)


Blackjack()