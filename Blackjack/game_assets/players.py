import random


class PlayerBase:
    def __init__(self):
        self._name = None
        self._credits = random.randint(10, 100)
        self._hand = []

    def say_hello(self):
        print(f"Hello, my name is {self._name}")

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