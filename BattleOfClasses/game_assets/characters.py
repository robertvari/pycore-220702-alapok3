import random
from game_assets.items import Weapon


class CharacterBase:
    race_list = {
        "human": {"strength": 20, "max_HP": 50},
        "ork": {"strength": 100, "max_HP": 130},
        "elf": {"strength": 30, "max_HP": 80},
        "dwarf": {"strength": 150, "max_HP": 130},
    }

    def __init__(self):
        self._name = None
        self._race = None

        self._golds = random.randint(0, 200)
        self._inventory = []
        self._right_hand = None

        self._strength = 0
        self._initiative = random.randint(10, 100)
        self._current_HP = 0
        self._max_HP = 0

        self._create()

    @property
    def name(self):
        return self._name

    @property
    def initiative(self):
        return self._initiative

    @property
    def current_HP(self):
        return self._current_HP

    def take_damage(self, damage):
        self._current_HP -= damage
        if self._current_HP < 0:
            self._current_HP = 0
            print(f"{self.name} is dead :(")

        print(f"{self._name} takes {damage} damage. Current HP: {self._current_HP}")

    def heal(self, value):
        self._current_HP += value
        if self._current_HP > self._max_HP:
            self._current_HP = self._max_HP

        print(f"{self._name} heals {value}. Current HP: {self._current_HP}")

    def give_items(self, item_list):
        for i in item_list:
            self._inventory.append(i)

            if not self._right_hand and isinstance(i, Weapon):
                self._right_hand = i

    def _create(self):
        self._name = self.get_fantasy_name()
        self._race = random.choice(list(self.race_list))
        self._strength = self.race_list[self._race]["strength"]
        self._max_HP = self.race_list[self._race]["max_HP"]
        self._current_HP = self._max_HP

    @staticmethod
    def get_fantasy_name():
        FIRST = ['A', 'Ag', 'Ar', 'Ara', 'Anu', 'Bal', 'Bil', 'Boro', 'Bern', 'Bra', 'Cas', 'Cere', 'Co', 'Con',
                 'Cor', 'Dag', 'Doo', 'Elen', 'El', 'En', 'Eo', 'Faf', 'Fan', 'Fara', 'Fre', 'Fro', 'Ga', 'Gala', 'Has',
                 'He', 'Heim', 'Ho', 'Isil', 'In', 'Ini', 'Is', 'Ka', 'Kuo', 'Lance', 'Lo', 'Ma', 'Mag', 'Mi', 'Mo',
                 'Moon', 'Mor', 'Mora', 'Nin', 'O', 'Obi', 'Og', 'Pelli', 'Por', 'Ran', 'Rud', 'Sam', 'She', 'Sheel',
                 'Shin', 'Shog', 'Son', 'Sur', 'Theo', 'Tho', 'Tris', 'U', 'Uh', 'Ul', 'Vap', 'Vish', 'Ya', 'Yo', 'Yyr']

        SECOND = ['ba', 'bis', 'bo', 'bus', 'da', 'dal', 'dagz', 'den', 'di', 'dil', 'din', 'do', 'dor', 'dra',
                  'dur', 'gi', 'gauble', 'gen', 'glum', 'go', 'gorn', 'goth', 'had', 'hard', 'is', 'ki', 'koon', 'ku',
                  'lad', 'ler', 'li', 'lot', 'ma', 'man', 'mir', 'mus', 'nan', 'ni', 'nor', 'nu', 'pian', 'ra', 'rak',
                  'ric', 'rin', 'rum', 'rus', 'rut', 'sek', 'sha', 'thos', 'thur', 'toa', 'tu', 'tur', 'tred', 'varl',
                  'wain', 'wan', 'win', 'wise', 'ya']

        return f"{random.choice(FIRST)}{random.choice(SECOND)}"

    def __str__(self):
        return f"===============  {self._name}  ================\n" \
               f"Race: {self._race}\n" \
               f"Golds: {self._golds}\n" \
               f"Inventory: {self._inventory}\n" \
               f"Right hand: {self._right_hand}\n" \
               f"Strength: {self._strength}\n" \
               f"Initiative: {self._initiative}\n" \
               f"Current HP: {self._current_HP}\n" \
               f"=======================================\n"


class Player(CharacterBase):
    def _create(self):
        self._name = "Robert"
        self._race = "human"

        while self._race not in list(self.race_list):
            self._race = input(f"What is your race? {list(self.race_list)}")

        self._strength = self.race_list[self._race]["strength"]
        self._max_HP = self.race_list[self._race]["max_HP"]
        self._current_HP = self._max_HP


class AIPlayer(CharacterBase):
    pass


if __name__ == '__main__':
    ai_player = AIPlayer()
    player = Player()

    print(ai_player)
    print(player)