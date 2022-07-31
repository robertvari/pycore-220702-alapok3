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
        self._name = f"{random.choice(first_names)} {random.choice(last_names)}"
        self._credits = random.randint(10, 100)

    def __str__(self):
        return f"Name: {self._name}\nCredits: {self._credits}\nCards: {self._hand}"


class Player(PlayerBase):
    def _create(self):
        # calls Base Class _create() to get everything from there.
        super()._create()
        self._name = input("What is your name?")


class AIPlayer(PlayerBase):
    pass


if __name__ == '__main__':
    player = Player()
    ai_player = AIPlayer()

    print(player)
    print(ai_player)