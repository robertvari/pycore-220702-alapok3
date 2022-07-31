class ItemBase:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def use(self, character):
        print("ItemBase use called!")

    def __str__(self):
        return f"Name: {self._name} Price: {self._price} golds\n"


class CommonItem(ItemBase):
    def use(self, character):
        print(f"{character.name} uses {self._name}")


class Food(ItemBase):
    def use(self, character):
        print(f"{character.name} eats {self._name}")


class Drink(ItemBase):
    def use(self, character):
        print(f"{character.name} drinks {self._name}")


class Weapon(ItemBase):
    def use(self, character):
        print(f"{character.name} attacks with a {self._name}")


if __name__ == '__main__':
    from game_assets.characters import AIPlayer

    bread = Food("Bread", 2)
    milk = Food("Milk", 4)
    stick = CommonItem("Stick", 1)
    sword = Weapon("Sword", 23)

    ai_player = AIPlayer()

    bread.use(ai_player)
    milk.use(ai_player)
    stick.use(ai_player)
    sword.use(ai_player)