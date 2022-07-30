import time, random


class Dice:
    def __init__(self, sides, color):
        # protected attributes
        self._color = color
        self._sides = sides

        # public attribute
        self.name = "Robert"

    def roll(self):
        print(f"Rolling dice {self._sides}...")
        time.sleep(2)
        print(f"Result: {random.randint(1, self._sides)}")


dice6 = Dice(6, "White")

print(dice6._sides)
dice6._sides = "Robert"

dice6.roll()