import random
from enum import Enum
from random import randint, choice


class SuperAbility(Enum)
    HEAL = 1
    BOOST = 2
    CRITICAL_DAMAGE = 3
    BLOCK_DAMAGE_AND_REVERT =


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def(self, value):
        self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    def choose_defence(self,heroes):
        random_hero = random.choice(heroes)
        self.__defence = random_hero.ability

    def attack(self, heroes):
        for hero in heroes
            hero.health -= self.damage

    @property
    def defence(self):
        return self.__defence

    def __str__(self):
        return super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        if isinstance(ability, SuperAbility)
            self.__ability = ability
        else:
            raise ValueError('Wrong Value')

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        boss.health -= self.damage

    def use_super_power(self, boss, heroes):
        pass

class Warrior(Hero):
    def __init__(self,name,health,damage):
        super().__init__(self,name,health,damage,SuperAbility.CRITICAL_DAMAGE)

    def use_super_power(self, boss, heroes):
        pass


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(self, name, health, damage, SuperAbility.BOOST)

    def use_super_power(self, boss, heroes):
        pass


class Medic (Hero):
    def __init__(self, name, health, damage,heal_points):
        super().__init__(self, name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def use_super_power(self, boss, heroes):
        pass

class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(self, name, health, damage, SuperAbility.BLOCK_DAMAGE_AND_REVERT)
        self.__block_damage = 0

    @property
    def block_damage(self):
        return self.__block_damage
    @block_damage.setter
    def block_damage(self, value):
        self.__block_damage = value

    def use_super_power(self, boss, heroes):
        pass

round_number = 0
def show_stats(boss, heroes)

def start_game
    boss = Boss('Roshan',1000,50)
    warrior = Warrior('Hercules',280,10)
    magic = Magic('Rubick',290,15)
    doc = Medic('AiBolit',250,15)
    berserk = Berserk(Pudge , 260, 10)
    assistent = Medic('Hous',300,10,5)