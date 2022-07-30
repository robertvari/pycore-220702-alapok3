class Dice:
    # class attribute
    used_for = "Used for playing tabletop games."

    def __init__(self, sides, color):
        # instance attribute
        self.color = color
        self.sides = sides


class Person:
    # class attribute for Person
    db = "employees"

    def __init__(self, name, age=None, address=None, email=None):
        # instance attributes
        self.name = name
        self.age = age
        self.address = address
        self.email = email


dice6 = Dice(6, "red")
dice20 = Dice(20, "blue")
dice10 = Dice(10, "green")

# print(dice6.sides, dice6.color)
# print(dice10.sides, dice10.color)
# print(dice20.sides, dice20.color)
#
# print(Dice.color, Dice.sides)
# Dice.color = "Yellow"
# print(Dice.color, Dice.sides)
#
# dice10.color = "BLUE"
# print(Dice.color, Dice.sides)

robert = Person("Robert")
csaba = Person("Csaba", 20)
kriszta = Person("Kriszta", 23, "Pécs")
tamas = Person("Tamás", 32, "Budapest", "tamas@gmail.com")

print(robert.name, robert.age, robert.address, robert.email)
print(csaba.name, csaba.age, csaba.address, csaba.email)
print(kriszta.name, kriszta.age, kriszta.address, kriszta.email)
print(tamas.name, tamas.age, tamas.address, tamas.email)

print(tamas.db, robert.db, kriszta.db, csaba.db)
Person.db = "Persons"
print(tamas.db, robert.db, kriszta.db, csaba.db)