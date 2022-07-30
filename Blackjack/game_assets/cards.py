import random


class Card:
    def __init__(self, name, value):
        self._name = name
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        assert isinstance(new_value, int), "Value must be of type int"
        assert new_value == 1, "Value must equal to 1"
        assert "Ace" in self._name, "This is not an Ace!"

        self._value = new_value

    def change_value(self):
        assert "Ace" in self._name, "This is not an Ace!"
        assert self._value > 1, "Value must be greater than 1"
        self._value = 1

    def __str__(self):
        return f"Name: {self._name} Value: {self._value}"

    def __repr__(self):
        return f"{self._name} {self._value}"


class Deck:
    def __init__(self):
        self._cards = []
        self.shuffle()

    def shuffle(self):
        self._cards.clear()

        cards = [
            ["2", 2],
            ["3", 3],
            ["4", 4],
            ["5", 5],
            ["6", 6],
            ["7", 7],
            ["8", 8],
            ["9", 9],
            ["10", 10],
            ["King", 10],
            ["Queen", 10],
            ["Jack", 10],
            ["Ace", 11]
        ]

        names = ["Heart", "Club", "Diamond", "Spade"]

        for name in names:
            for card_data in cards:
                card_name = f"{name} {card_data[0]}"
                value = card_data[1]
                new_card = Card(card_name, value)
                self._cards.append(new_card)

        random.shuffle(self._cards)

    def draw(self):
        new_card = self._cards[0]
        self._cards.remove(new_card)
        return new_card

    @property
    def card_number(self):
        return len(self._cards)

    def __str__(self):
        return f"{self._cards}"


if __name__ == '__main__':
    deck = Deck()