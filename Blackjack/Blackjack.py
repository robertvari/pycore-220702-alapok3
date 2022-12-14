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
        print("-"*100)
        players_in_turn = [player for player in self._players if player.count_hand() <= 21]

        if not players_in_turn:
            print("Nobody wins this time :(")
        else:
            winner_list = sorted(players_in_turn, key=lambda player: player.count_hand())
            winner = winner_list[-1]

            print(f"The winner is: {winner.name}")
            winner.give_reward(self._reward)

        print("-" * 100)
        player_input = input("Do you want to play a new round? (y/n)")
        if player_input == "y":
            self._start_game()
        else:
            self._exit_game()

    @staticmethod
    def _exit_game():
        print("Have a nice day!")
        exit()

    @staticmethod
    def __intro():
        print("-" * 50, "BLACKJACK", "-" * 50)


Blackjack()
