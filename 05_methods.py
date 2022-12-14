import time, random


class Person:
    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email

    # this is a method for a Person
    def greeting(self):
        print(f"Hello! My name is {self.name}")

    def report(self):
        print(f"My name is: {self.name}")
        print(f"I live in: {self.address}")
        print(f"My email is: {self.email}")


class Dice:
    def __init__(self, sides, color):
        self.sides = sides
        self.color = color

    def roll(self):
        print(f"Rolling with dice {self.sides}")
        time.sleep(1)
        print(f"Result: {random.randint(1, self.sides)}")


tamas = Person("Kiss Tamás", "Budapes", "tamas@gmail.com")
kriszta = Person("Nagy Krisztina", "Pécs", "kriszta@gmail.com")


dice6 = Dice(6, "White")
dice20 = Dice(20, "Blue")
dice10 = Dice(10, "Green")

dice6.roll()
dice20.roll()
dice10.roll()