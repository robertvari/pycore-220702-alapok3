import random


class PlayerBase:
    def __init__(self):
        # create attributes with default values
        self._name = None
        self._credits = 0
        self._hand = []
        self._in_game = True

        # start methods
        self._create()

    def _create(self):
        first_names = ["Brittney", "Curtis", "Lucas", "Chip", "Simon"]
        last_names = ["Moriah", "Tristin", "Troy", "Gale", "Lynn"]

    def __str__(self):
        return f"Name: {self._name}\nCredits: {self._credits}\nCards: {self._hand}"


class Player(PlayerBase):
    pass


class AIPlayer(PlayerBase):
    pass


if __name__ == '__main__':
    player = Player()
    ai_player = AIPlayer()

    player.say_hello()
    ai_player.say_hello()