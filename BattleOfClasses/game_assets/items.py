import json


class ItemBase:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def use(self, character):
        print("ItemBase use called!")

    @staticmethod
    def generate_item_list():
        with open("game_assets/item_list.json") as f:
            item_data = json.load(f)

        item_list = []
        for item_name, data in item_data.items():
            price = data["price"]
            item_type = data["type"]
            if item_type == "Weapon":
                new_item = Weapon(item_name, price)
            elif item_type == "Food":
                new_item = Food(item_name, price)
            elif item_type == "Drink":
                new_item = Drink(item_name, price)
            else:
                new_item = CommonItem(item_name, price)

            item_list.append(new_item)

        return item_list

    def __str__(self):
        return f"Name: {self._name} Price: {self._price} golds\n"

    def __repr__(self):
        return self._name


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
        print(f"{self._name} damage: {character}")
        character.take_damage(20)


if __name__ == '__main__':
    item_list = ItemBase.generate_item_list()
    print(item_list)