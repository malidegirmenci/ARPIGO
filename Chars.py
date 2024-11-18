from abc import ABC, abstractmethod

from Items import Weapon


# Parent Abstract Class
class Character(ABC):
    def __init__(self, name, health, armor, attack_power, weapon):
        self.__name = name
        self.__health = health
        self.__armor = armor
        self.__attack_power = attack_power
        self.__weapon = weapon

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_health(self):
        return self.__health

    def set_health(self, health):
        self.__health = health

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

    def show_info(self):
        print(f'Name:{self.__name}\nHealth: {self.__health}\nArmor:{self.__armor}\nAttack Power:{self.get_attack_power()}')


    def special_skill(self):
        pass

    def damage(self, target):
        return self.__attack_power - target.__armor

# Player Characters
class SwordMaster(Character):
    def __init__(self, name):
        dual_swords = Weapon('Dual Swords', 65, 100, 1.7)
        super().__init__(name, 80, 30,  15, dual_swords)

class Archer(Character):
    def __init__(self, name, weapon):
        super().__init__(name, 70, 25,  10, weapon)

class Wizard(Character):
    def __init__(self, name, weapon):
        super().__init__(name, 50, 15, 5, weapon)

class Cleric(Character):
    def __init__(self, name):
        super().__init__(name, 60, 40, 70)

class Assassin(Character):
    def __init__(self, name, ):
        super().__init__(name, 75, 30, 60)

class Tank(Character):
    def __init__(self, name):
        super().__init__(name, 100, 50,  70)

class Warlock(Character):
    def __init__(self, name,):
        super().__init__(name,50, 25, 80)

#--------------------

# Monster Characters
class GeneralMonster(Character):
    def __init__(self, name, health, armor,  attack_power):
        super().__init__(name,health,armor, attack_power)

class UniqueMonster(Character):
    def __init__(self, name, health, armor, attack_power):
        super().__init__(name,health,armor, attack_power)