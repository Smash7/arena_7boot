import copy
import random
import math
from classes import Paladin, Warrior, Thing
from colorama import init
from colorama import Fore, Style


init()

# Шаг 1 - создаем произвольное количество вещей с различными параметрами,
# процент защиты не должен превышать 10%(0.1).
# Сортируем по проценту защиты, по возрастанию;
things = []
names_things = [
    "Shield", "Sword", "Armor",
    "Amulet", "Bow", "blade", "Helmet",
    "Gloves", "Sheath", "Hauberk"
]
descriptions_things = [
    "Durable", "Strong", "Heavy", "Ancients",
    "Damned", "Small", "Effective", "Simple",
    "Faithful", "Selected"
]
quantity_persons = int(input("Выберете количество персонажей:"))
quantity_items = quantity_persons * 4

for _ in range(quantity_items):
    name = random.choice(names_things) + random.choice(descriptions_things)
    protection_percent = random.uniform(0.01, 0.10)
    attack = random.randint(1, 20)
    hp = random.randint(5, 100)
    new_thing = Thing(name, protection_percent, attack, hp)
    things.append(new_thing)

things.sort(key=lambda x: x.protection_percent)

# Шаг 2 - создаем произвольно 10 персонажей,
# кол-во воинов и паладинов произвольно.
# Имена персонажам тоже рандомные из созданного списка 20 имен.
names = [
    "John", "Alice", "Bob", "Charlie", "David",
    "Eve", "Frank", "Grace", "Heidi", "Ivan",
    "Jacob", "Kate", "Leo", "Mia", "Nick",
    "Olivia", "Peter", "Rachel", "Sam", "Tina"
]
characters = []
for _ in range(quantity_persons):
    name = random.choice(names)
    while name in characters:
        name = random.choice(names)
    hp = random.randint(100, 200)
    base_attack = random.randint(10, 20)
    base_protection = random.uniform(0.01, 0.05)
    character_class = random.choice([Paladin, Warrior])
    new_character = character_class(name, hp, base_attack, base_protection)
    characters.append(new_character)

# Шаг 3 - одеваем персонажей рандомными вещами.
# Кому-то 1, кому-то больше, но не более 4 вещей в одни руки;
for character in characters:
    thing_count = random.randint(1, 4)
    character_things = random.sample(things, thing_count)
    character.set_things(character_things)

# Шаг 4 - отправляем персонажей на арену, и в цикле в произвольном порядке
# выбирается пара Нападающий и Защищающийся.
arena = copy.deepcopy(characters)
while len(arena) > 1:
    attacker = random.choice(arena)
    defender = random.choice(arena)
    while attacker == defender:
        defender = random.choice(arena)

    attack_damage = attacker.get_total_attack()
    final_protection = defender.get_total_protection()
    damage = attack_damage - attack_damage * final_protection

    defender.take_damage(damage)
    print(Fore.RED + Style.BRIGHT +
          f"{attacker.name} наносит удар по {defender.name} "
          f"{damage:.2f} урона \n",
          Fore.GREEN + f"У {defender.name} осталось "
          f"{math.ceil(defender.hp)}HP")

    if defender.hp <= 0:
        print(Fore.BLACK + Style.BRIGHT + f"{defender.name} погиб")
        arena.remove(defender)

print(Fore.YELLOW + Style.BRIGHT + f"Победитель: {arena[0].name}")
