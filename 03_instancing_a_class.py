class Dice:
    # class attributes
    sides = 6
    color = "white"


class Person:
    # class attribute
    name = "Robert"

# create two instances of Dice
dice6 = Dice()

# change default attributes for dice20
dice20 = Dice()
dice20.sides = 20
dice20.color = "red"

# print(dice6.sides)
# print(dice6.color)
#
# print(dice20.sides)
# print(dice20.color)


robert = Person()
print(robert.name)

tamas = Person()
tamas.name = "Tamás"
print(tamas.name)


print(Person.name)