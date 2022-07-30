class Dice:
    # class attributes
    sides = 6
    color = "white"


class Person:
    # class attributes
    name = "Robert"
    age = 36
    address = "Budapest"
    email = "robert@gmail.com"


# print(Dice.color)
# print(Dice.sides)
#
# Dice.color = "Red"
#
# print(Dice.color)
# print(Dice.sides)


print(Person.name)
print(Person.age)
print(Person.email)
print(Person.address)

Person.name = "Tamás"
print(Person.name)