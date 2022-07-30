import time, random


class Dice:
    colors = ["white", "blue", "green", "red"]

    def __init__(self, sides, color):
        # private attributes
        self.__color = color
        self.__sides = sides

    def roll(self):
        print(f"Rolling dice {self.__sides}...")
        time.sleep(2)
        print(f"Result: {random.randint(1, self.__sides)}")

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        assert new_color in Dice.colors, f"Colors must be: {Dice.colors}"
        self.__color = new_color

    @property
    def sides(self):
        return self.__sides

    def __str__(self):
        return f"Color: {self.__color} Sides: {self.__sides}"


dice6 = Dice(6, "White")
print(dice6.color)
dice6.color = "green"
print(dice6.color)