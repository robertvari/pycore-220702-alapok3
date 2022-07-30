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


dice6 = Dice(6, "White")