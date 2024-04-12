import Person


class Warrior(Person):
    def __init__(self, name, hp, base_attack, base_protection):
        super().__init__(name, hp, base_attack * 2, base_protection)
