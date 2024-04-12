class Person:
    def __init__(self, name, hp, base_attack, base_protection):
        self.name = name
        self.hp = hp
        self.base_attack = base_attack
        self.base_protection = base_protection
        self.things = []

    def set_things(self, things):
        self.things = things
        for thing in things:
            self.hp += thing.hp

    def get_total_attack(self):
        total_attack = self.base_attack
        for thing in self.things:
            total_attack += thing.attack
        return total_attack

    def get_total_protection(self):
        total_protection = self.base_protection
        for thing in self.things:
            total_protection += thing.protection_percent
        return total_protection

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def __str__(self):
        return f"{self.name} (HP: {self.hp}, "
        "Attack: {self.get_total_attack()}, "
        "Protection: {self.get_total_protection()})"


class Warrior(Person):
    def __init__(self, name, hp, base_attack, base_protection):
        super().__init__(name, hp, base_attack * 2, base_protection)


class Thing:
    def __init__(self, name, protection_percent, attack, hp):
        self.name = name
        self.protection_percent = protection_percent
        self.attack = attack
        self.hp = hp

    def __str__(self):
        return f"{self.name} (Protection: {self.protection_percent}, "
        f"Attack: {self.attack}, HP: {self.hp})"


class Paladin(Person):
    def __init__(self, name, hp, base_attack, base_protection):
        super().__init__(name, hp * 2, base_attack, base_protection * 2)
