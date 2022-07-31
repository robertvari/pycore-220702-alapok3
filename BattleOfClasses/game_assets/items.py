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


class Consumable(ItemBase):
    def use(self, character):
        character.heal(20)


class Food(Consumable):
    def use(self, character):
        print(f"{character.name} eats {self._name}")
        super().use(character)


class Drink(Consumable):
    def use(self, character):
        print(f"{character.name} drinks {self._name}")
        super().use(character)


class Weapon(ItemBase):
    def use(self, character):
        print(f"{character.name} attacks with a {self._name}")


if __name__ == '__main__':
    from game_assets.characters import AIPlayer

    bread = Food("Bread", 2)
    milk = Drink("Milk", 4)

    ai_player = AIPlayer()
    ai_player.take_damage(34)
    ai_player.take_damage(10)

    bread.use(ai_player)
    milk.use(ai_player)