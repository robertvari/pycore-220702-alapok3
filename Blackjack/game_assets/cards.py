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
    pass


if __name__ == '__main__':
    card1 = Card("Spade King", 10)
    card2 = Card("Club 2", 2)
    card3 = Card("Diamond Ace", 11)

    card3.change_value()
    print(card3)