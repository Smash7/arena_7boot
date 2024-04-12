class Person:
    """
    Базовый класс для персонажей.

    :param name: Имя персонажа
    :type name: str
    :param hp: Базовое количество жизней
    :type hp: int
    :param base_attack: Базовая атака
    :type base_attack: int
    :param base_protection: Базовый процент защиты
    :type base_protection: float
    """

    def __init__(self, name, hp, base_attack, base_protection):
        self.name = name
        self.hp = hp
        self.base_attack = base_attack
        self.base_protection = base_protection
        self.things = []

    def set_things(self, things):
        """
        Устанавливает список вещей персонажу и
        увеличивает жизни персонажа в соответствии с жизнями вещей.

        :param things: Список вещей
        :type things: list[Thing]
        """
        self.things = things
        for thing in things:
            self.hp += thing.hp

    def get_total_attack(self):
        """
        Возвращает общую атаку персонажа вместе с вещами.

        :return: Общая атака
        :rtype: int
        """
        total_attack = self.base_attack
        for thing in self.things:
            total_attack += thing.attack
        return total_attack

    def get_total_protection(self):
        """
        Возвращает общий процент защиты персонажа вместе с вещами.

        :return: Общий процент защиты
        :rtype: float
        """
        total_protection = self.base_protection
        for thing in self.things:
            total_protection += thing.protection_percent
        return total_protection

    def take_damage(self, damage):
        """
        Вычитает жизни персонажа в зависимости от полученного урона.

        :param damage: Урон
        :type damage: float
        """
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def __str__(self):
        """
        Возвращает строковое представление персонажа.

        :return: Строковое представление
        :rtype: str
        """
        return (
            f"{self.name} (HP: {self.hp}, "
            "Attack: {self.get_total_attack()}, "
            "Protection: {self.get_total_protection()})"
        )


class Warrior(Person):
    """
    Класс Воина, наследующийся от базового класса Person.

    :param name: Имя персонажа
    :type name: str
    :param hp: Базовое количество жизней
    :type hp: int
    :param base_attack: Базовая атака
    :type base_attack: int
    :param base_protection: Базовый процент защиты
    :type base_protection: float
    """

    def __init__(self, name, hp, base_attack, base_protection):
        super().__init__(name, hp, base_attack * 2, base_protection)


class Thing:
    """
    Класс Вещи.

    :param name: Название вещи
    :type name: str
    :param protection_percent: Процент защиты
    :type protection_percent: float
    :param attack: Атака
    :type attack: int
    :param hp: Количество жизней
    :type hp: int
    """

    def __init__(self, name, protection_percent, attack, hp):
        self.name = name
        self.protection_percent = protection_percent
        self.attack = attack
        self.hp = hp

    def __str__(self):
        """
        Возвращает строковое представление вещи.

        :return: Строковое представление
        :rtype: str
        """
        return (
            f"{self.name} (Protection: {self.protection_percent}, "
            f"Attack: {self.attack}, HP: {self.hp})"
        )


class Paladin(Person):
    """
    Класс Паладина, наследующийся от базового класса Person.

    :param name: Имя персонажа
    :type name: str
    :param hp: Базовое количество жизней
    :type hp: int
    :param base_attack: Базовая атака
    :type base_attack: int
    :param base_protection: Базовый процент защиты
    :type base_protection: float
    """

    def __init__(self, name, hp, base_attack, base_protection):
        super().__init__(name, hp * 2, base_attack, base_protection * 2)
