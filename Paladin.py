import Person


class Paladin(Person):
    def __init__(self, name, hp, base_attack, base_protection):
        super().__init__(name, hp * 2, base_attack, base_protection * 2)
