class Card:
    def __init__(self, name, value):
        self._name = name
        self._value = value

    def __str__(self):
        return f"Name: {self._name} Value: {self._value}"

    def __repr__(self):
        return f"{self._name} {self._value}"

class Deck:
    pass


if __name__ == '__main__':
    card1 = Card("Spade King", 10)
    card2 = Card("Club 2", 2)
    card3 = Card("Diamond Ace", 11)

    my_hand = [card1, card2, card3]
    print(my_hand)