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


class Person:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__payments = [10, 20, 45, 20, 60, 80]

    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    @property
    def avarage_sallary(self):
        all_payments_sum = sum(self.__payments)
        return all_payments_sum / len(self.__payments)

    def __str__(self):
        return f"{self.__first_name} {self.__last_name}"


csaba = Person("Kiss", "Csaba")
print(csaba.full_name)
print(csaba.avarage_sallary)