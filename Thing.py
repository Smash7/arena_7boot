class Thing:
    def __init__(self, name, protection_percent, attack, hp):
        self.name = name
        self.protection_percent = protection_percent
        self.attack = attack
        self.hp = hp

    def __str__(self):
        return f"{self.name} (Protection: {self.protection_percent}, "
        f"Attack: {self.attack}, HP: {self.hp})"
