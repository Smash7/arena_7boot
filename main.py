import random
import Paladin
import Thing
import Warrior


def battle():
    # Шаг 1 - создаем произвольное количество вещей с различными параметрами,
    # процент защиты не должен превышать 10%(0.1).
    # Сортируем по проценту защиты, по возрастанию;
    things = [
        Thing("Shield", 0.08, 0, 100),
        Thing("Sword", 0, 20, 80),
        Thing("Armor", 0.1, 0, 120),
        Thing("Ring", 0.05, 5, 50),
        Thing("Amulet", 0.03, 3, 30),
    ]
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
    for _ in range(10):
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
    arena = characters.copy()
    while len(arena) > 1:
        attacker = random.choice(arena)
        defender = random.choice(arena)
        while attacker == defender:
            defender = random.choice(arena)

        attack_damage = attacker.get_total_attack()
        final_protection = defender.get_total_protection()
        damage = attack_damage - attack_damage * final_protection

        print(f"{attacker.name} наносит удар по {defender.name} "
              f"на {damage:.2f} урона")
        defender.take_damage(damage)

        if defender.hp <= 0:
            print(f"{defender.name} погиб")
            arena.remove(defender)

    print(f"Победитель: {arena[0].name}")