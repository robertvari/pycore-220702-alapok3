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

    def __str__(self):
        return f"Color: {self.__color} Sides: {self.__sides}"


dice6 = Dice(6, "White")
print(dice6)

print(dice6.get_color())
print(dice6.get_sides())

dice6.__color = "Red"
print(dice6.get_color())