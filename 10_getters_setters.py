import time, random


class Dice:
    def __init__(self, sides, color):
        # private attributes
        self.__color = color
        self.__sides = sides

    def roll(self):
        print(f"Rolling dice {self.__sides}...")
        time.sleep(2)
        print(f"Result: {random.randint(1, self.__sides)}")

    # this is a getter for the __sides attribute
    def get_sides(self):
        return self.__sides

    def get_color(self):
        return self.__color

    def set_sides(self, new_sides):
        assert isinstance(new_sides, int), "sides must be of type int"
        assert new_sides >= 1, "sides must be greater or equal to 1"
        self.__sides = new_sides

    def __str__(self):
        return f"Color: {self.__color} Sides: {self.__sides}"


dice6 = Dice(6, "White")
dice6.set_sides(-10)
print(dice6)