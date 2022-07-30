class Dice:
    # class attribute
    used_for = "Used for playing tabletop games."

    def __init__(self, sides, color):
        # instance attribute
        self.color = color
        self.sides = sides




dice6 = Dice(6, "red")
dice20 = Dice(20, "blue")
dice10 = Dice(10, "green")

print(dice6.sides, dice6.color)
print(dice10.sides, dice10.color)
print(dice20.sides, dice20.color)

print(Dice.color, Dice.sides)
Dice.color = "Yellow"
print(Dice.color, Dice.sides)

dice10.color = "BLUE"
print(Dice.color, Dice.sides)