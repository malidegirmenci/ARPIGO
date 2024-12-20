from abc import ABC, abstractmethod

from Helper import show_message
from Items import Weapon, Armor, hands, basic_armor

import random

# Parent Abstract Class
class Character(ABC):
    def __init__(self, name, health, defence, attack_power, weapon, armor, type_of_char):
        self.__name = name
        self.__health = health
        self.__defence = defence
        self.__attack_power = attack_power
        self.__weapon = weapon
        self.__armor = armor
        self.__coin = 0
        self.__type_of_char = type_of_char
        self.__inventory = []
        self.__quest_items = []

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_health(self):
        if self.__health < 0:
            return 0
        return self.__health

    def set_health(self, health):
        self.__health = health

    def get_defence(self):
        total_defence = self.__defence + self.__armor.get_defence()
        return total_defence

    def set_defence(self, defence):
        self.__defence = defence

    def get_armor(self):
        return self.__armor

    def set_armor(self, armor):
        self.__armor = armor

    def get_attack_power(self):
        total_attack_power = self.__attack_power + self.__weapon.get_attack_power()
        return total_attack_power

    def set_attack_power(self, attack_power):
        self.__attack_power = attack_power

    def get_weapon(self):
        return self.__weapon

    def set_weapon(self, weapon):
        self.__weapon = weapon

    def get_coin(self):
        return self.__coin

    def set_coin(self, coin):
        self.__coin = coin

    def get_type_of_char(self):
        return self.__type_of_char

    def get_inventory(self):
        return self.__inventory

    def get_quest_items(self):
        return self.__quest_items

    def add_quest_items(self, quest_item):
        self.__quest_items.append(quest_item)

    def add_item_in_inventory(self, item):
        self.__inventory.append(item)
        show_message(f'{self.get_name()} envanterine {item.get_name()} ekledi')

    def remove_item_in_inventory(self, item):
        self.__inventory.remove(item)

    def show_info(self):
        print(f'{self.get_type_of_char()}')
        print(f'Name:{self.get_name()}\nHealth: {self.get_health()}\nDefence:{self.get_defence()}\nAttack Power:{self.get_attack_power()}')

    @abstractmethod
    def special_skill(self):
        pass

    def damage(self, target):
        base_damage = self.get_attack_power() - target.get_defence()
        min_damage = base_damage - 10
        max_damage = base_damage + 10
        last_damage = random.randint(min_damage, max_damage)
        if last_damage >= 0:
            return last_damage
        return 0

    def take_weapon(self, weapon):
        self.set_weapon(weapon)
        print(f'{weapon.get_name()} [Fışşınk] kuşanıldı.')

    def remove_weapon(self):
        print(f'{self.get_weapon().get_name()} çıkarıldı')
        self.set_weapon(hands)

    def take_armor(self, armor):
        self.set_armor(armor)
        print(f'{armor.get_name()} [Fışşınk] kuşanıldı.')

    def remove_armor(self):
        print(f'{self.get_armor().get_name()} çıkarıldı')
        self.set_armor(basic_armor)

    def show_inventory(self):
        for item in self.__inventory:
            if item.get_type_of_item() == 'armor':
                item.show_armor()
            elif item.get_type_of_item() == 'weapon':
                item.show_weapon()
            else:
                print('Invalid key')

# Player Characters
class SwordMaster(Character):
    def __init__(self, name):
        dual_swords = Weapon('Dual Swords', 85, 100, 1.7)
        dual_swords.set_is_equipped(True)
        heavy_armor = Armor('Heavy Armor', 65, 100, 1.7)
        heavy_armor.set_is_equipped(True)

        super().__init__(name, 80, 30,  15, dual_swords, heavy_armor, 'Sword Master')

    def special_skill(self):
        return self.get_attack_power() * 2

class Archer(Character):
    def __init__(self, name):
        bow = Weapon('Bow', 90, 100, 1.6)
        armor = Armor('Light Armor', 65, 100, 1.7)
        super().__init__(name, 70, 25,  10, bow, armor, 'Archer')

    def special_skill(self):
        return self.get_attack_power() + (self.get_attack_power() * 1.45)

class Wizard(Character):
    def __init__(self, name):
        staff = Weapon('Staff', 40, 100, 1)
        armor = Armor('Robe', 65, 100, 1.7)
        super().__init__(name, 50, 15, 5, staff, armor, 'Wizard')

    def special_skill(self):
        return self.get_attack_power() * 3
'''
class Cleric(Character):
    def __init__(self, name):
        magic_wand = Weapon('Magic Wand', 60, 100, 1)
        super().__init__(name, 60, 40, 10, magic_wand)

class Assassin(Character):
    def __init__(self, name, ):
        dagger = Weapon('Dagger', 50, 100, 1.8)
        super().__init__(name, 75, 30, 60, dagger)

class Tank(Character):
    def __init__(self, name):
        sword = Weapon('Sword', 40, 100, 1.4)
        super().__init__(name, 100, 50,  15, sword)

class Warlock(Character):
    def __init__(self, name,):
        dark_staff = Weapon('Dark staff', 80, 100, 1)
        super().__init__(name,50, 25, 10, dark_staff)
'''
#--------------------
class Monster(ABC):
    def __init__(self, name, health, defence, attack_power, reward):
        self.__name = name
        self.__health = health
        self.__defence = defence
        self.__attack_power = attack_power
        self.__reward = reward

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_health(self):
        if self.__health < 0:
            return 0
        return self.__health

    def set_health(self, health):
        self.__health = health

    def get_defence(self):
        return self.__defence

    def set_defence(self, defence):
        self.__defence = defence

    def get_attack_power(self):
        return self.__attack_power

    def set_attack_power(self, attack_power):
        self.__attack_power = attack_power

    def get_reward(self):
        return self.__reward

    def show_info(self):
        print(f'Name:{self.get_name()}\nHealth: {self.get_health()}\nDefence:{self.get_defence()}\nAttack Power:{self.get_attack_power()}')

    def damage(self, target):
        base_damage = self.get_attack_power() - target.get_defence()
        min_damage = base_damage - 10
        max_damage = base_damage + 10
        last_damage = random.randint(min_damage, max_damage)
        if last_damage > 0:
            return last_damage
        return 0

# Monster Characters
class GeneralMonster(Monster):
    def __init__(self, name, health, defence, attack_power, reward):
        super().__init__(name,health,defence, attack_power, reward)

class UniqueMonster(Monster):
    def __init__(self, name, health, defence, attack_power, reward, quest_item):
        super().__init__(name,health,defence, attack_power, reward)
        self.__quest_item = quest_item

    def get_quest_item(self):
        return self.__quest_item

    def special_skill(self):
        pass