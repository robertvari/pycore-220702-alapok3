import random
import time


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

    def draw_cards(self, deck):
        print("-"*20, f"{self._name} turn", "-"*20)

        while self._in_game:
            hand_value = self.count_hand()

            if hand_value < random.randint(16, 19):
                print(f"{self._name} draws a card...")
                time.sleep(1)
                new_card = deck.draw()

                if hand_value > 10 and new_card.value == 11:
                    new_card.change_value()
                self._hand.append(new_card)
            else:
                print(f"{self._name} passes...")
                self._in_game = False

    def count_hand(self):
        return sum([card.value for card in self._hand])

    def __str__(self):
        return f"Name: {self._name}\nCredits: {self._credits}\nCards: {self._hand}\nHand Value: {self.count_hand()}"


class Player(PlayerBase):
    def _create(self):
        # calls Base Class _create() to get everything from there.
        super()._create()
        # todo remove this comment!!! self._name = input("What is your name?")
        self._name = "Robert Vari"

    def draw_cards(self, deck):
        print("This is your torn!")

        while self._in_game:
            print(f"Your cards: {self._hand}")
            print(f"Hand value: {self.count_hand()}")

            player_input = input("Do you want to draw a new card? (y/n)")

            if player_input == "y":
                new_card = deck.draw()
                print(f"Your new card: {new_card}")

                if new_card.value == 11 and self.count_hand() > 10:
                    new_card.change_value()

                self._hand.append(new_card)
            else:
                self._in_game = False

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
    reward += player.give_bet()
    reward += ai_player.give_bet()

    # start player turns
    player_list = [player, ai_player]
    for p in player_list:
        p.draw_cards(deck)

    print(player)
    print(ai_player)