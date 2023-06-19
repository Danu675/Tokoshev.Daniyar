import random

class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, boss):
        pass

    def receive_damage(self, damage):
        pass

    def is_alive(self):
        return self.health > 0


class Boss:
    def __init__(self):
        self.health = 100

    def attack(self):
        return random.randint(5, 20)

    def receive_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0


class Warrior(Hero):
    def __init__(self, name, health):
        super().__init__(name, health)

    def attack(self, boss):
        damage = random.randint(10, 20)
        if random.random() < 0.3:  # 30% шанс критического удара
            damage *= random.uniform(1.5, 2.5)  # умножаем урон на случайный коэффициент
        boss.receive_damage(damage)
        print(f"{self.name} атакует босса и наносит {damage} урона.")


class Berserk(Hero):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.blocked_damage = 0

    def attack(self, boss):
        damage = random.randint(15, 25)
        boss.receive_damage(damage)
        self.blocked_damage += damage * 0.3
        print(f"{self.name} атакует босса и наносит {damage} урона.")

    def use_super_ability(self, boss):
        boss.receive_damage(self.blocked_damage)
        print(f"{self.name} использует свою суперспособность и возвращает боссу {self.blocked_damage} заблокированного урона.")
        self.blocked_damage = 0


class Magic(Hero):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.attack_increase = 0

    def attack(self, boss):
        damage = random.randint(5, 15) + self.attack_increase
        boss.receive_damage(damage)
        print(f"{self.name} атакует босса и наносит {damage} урона.")

    def increase_attack(self):
        self.attack_increase += random.randint(1, 5)
        print(f"{self.name} увеличивает свою атаку на {self.attack_increase}.")


class Thor(Hero):
    def __init__(self, name, health):
        super().__init__(name, health)

    def attack(self, boss):
        damage = random.randint(10, 20)
        if random.random() < 0.2:  # 20% шанс оглушения босса
            print("Босс оглушен!")
            return
        boss.receive_damage(damage)
        print(f"{self.name} атакует босса и наносит {damage} урона.")


class Golem(Hero):
    def __init__(self, name, health):
        super().__init__(name, health)

    def attack(self, boss):
        damage = random.randint(5, 10)
        boss.receive_damage(damage)
        print(f"{self.name} атакует босса и наносит {damage} урона.")

    def receive_damage(self, damage):
        self.health -= damage * 0.2
        print(f"{self.name} получает урон в размере {damage * 0.2}.")


class Witcher(Hero):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.revived_hero = None

    def attack(self, boss):
        print(f"{self.name} не наносит урон боссу.")

    def receive_damage(self, damage):
        self.health -= damage
        if self.health <= 0 and self.revived_hero is None:
            self.revived_hero = random.choice(heroes)
            print(f"{self.name} погибает, но оживляет героя {self.revived_hero.name}!")
            self.revived_hero.health = 1

    def is_alive(self):
        return super().is_alive() or (self.revived_hero is not None and self.revived_hero.is_alive())


class Avrora(Hero):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.invisible_rounds = 2
        self.damage_returned = 0

    def attack(self, boss):
        if self.invisible_rounds > 0:
            print(f"{self.name} находится в режиме невидимости и не наносит урон боссу.")
            self.damage_returned += boss.attack()
            self.invisible_rounds -= 1
        else:
            damage = random.randint(10, 20)
            boss.receive_damage(damage)
            print(f"{self.name} атакует босса и наносит {damage} урона.")

    def receive_damage(self, damage):
        if self.invisible_rounds > 0:
            self.damage_returned += damage
            print(f"{self.name} находится в режиме невидимости и возвращает боссу {self.damage_returned} урона.")
        else:
            self.health -= damage
            print(f"{self.name} получает урон в размере {damage}.")

    def is_alive(self):
        return super().is_alive() or self.invisible_rounds > 0


def fight(boss, heroes):
    while boss.is_alive() and any(hero.is_alive() for hero in heroes):
        for hero in heroes:
            if hero.is_alive():
                hero.attack(boss)
                if not boss.is_alive():
                    print(f"{hero.name} победил!")
                    return
        damage = boss.attack()
        for hero in heroes:
            if hero.is_alive():
                hero.receive_damage(damage)
                if not hero.is_alive():
                    print(f"{hero.name} погиб!")
                    break

    if boss.is_alive():
        print("Босс победил!")


if __name__ == "__main__":
    boss = Boss()
    warrior = Warrior("Воин", 100)
    berserk = Berserk("Берсерк", 120)
    magic = Magic("Маг", 80)
    thor = Thor("Тор", 90)
    golem = Golem("Голем", 150)
    witcher = Witcher("Ведьмак", 100)
    avrora = Avrora("Аврора", 100)

    heroes = [warrior, berserk, magic, thor, golem, witcher, avrora]

    print("Битва начинается!")

    round_number = 1
    while boss.is_alive() and any(hero.is_alive() for hero in heroes):
        print(f"\n--- Раунд {round_number} ---")
        print(f"Здоровье босса: {boss.health}")
        for hero in heroes:
            if hero.is_alive():
                hero.attack(boss)
        boss.attack()
        round_number += 1

    if boss.is_alive():
        print("\nБосс победил!")
    else:
        print("\nГерои победили!")
