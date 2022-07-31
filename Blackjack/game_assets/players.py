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

    @property
    def in_game(self):
        return self._in_game

    def _create(self):
        first_names = ["Brittney", "Curtis", "Lucas", "Chip", "Simon"]
        last_names = ["Moriah", "Tristin", "Troy", "Gale", "Lynn"]
        self._name = f"{random.choice(first_names)} {random.choice(last_names)}"
        self._credits = random.randint(10, 100)

    def init_hand(self, deck):
        self._hand = [
            deck.draw(),
            deck.draw()
        ]

    def give_bet(self):
        bet = 10

        if bet > self._credits:
            print(f"{self._name} passes. No credits left :(")
            self._in_game = False
            return 0  # early return with 0

        self._credits -= bet
        return bet

    def __str__(self):
        return f"Name: {self._name}\nCredits: {self._credits}\nCards: {self._hand}"


class Player(PlayerBase):
    def _create(self):
        # calls Base Class _create() to get everything from there.
        super()._create()
        # todo remove this comment!!! self._name = input("What is your name?")
        self._name = "Robert Vari"


class AIPlayer(PlayerBase):
    pass


if __name__ == '__main__':
    from game_assets.cards import Deck
    deck = Deck()
    reward = 0

    # create two players
    player = Player()
    ai_player = AIPlayer()

    # set start hand
    player.init_hand(deck)
    ai_player.init_hand(deck)

    # give bet
    # reward += player.give_bet()
    # reward += ai_player.give_bet()

    for _ in range(20):
        ai_player.give_bet()
        if not ai_player._in_game:
            break

    # start player turns
