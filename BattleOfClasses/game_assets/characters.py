import random


class CharacterBase:
    race_list = {
        "human": {"strength": 20},
        "ork": {"strength": 100},
        "elf": {"strength": 30},
        "dwarf": {"strength": 150},
    }

    def __init__(self):
        self._name = None
        self._race = None

        self._golds = random.randint(0, 200)
        self._inventory = []
        self._right_hand = None

        self._strength = 0
        self._initiative = 0

        self._create()

    def _create(self):
        self._name = self.get_fantasy_name()
        self._initiative = random.randint(10, 100)
        self._race = random.choice(list(self.race_list))
        self._strength = self.race_list[self._race]["strength"]

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
               f"=======================================\n"


class Player(CharacterBase):
    pass


class AIPlayer(CharacterBase):
    pass


if __name__ == '__main__':
    ai_player = AIPlayer()

    print(ai_player)