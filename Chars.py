from abc import ABC, abstractmethod

# Parent Abstract Class
class Character(ABC):
    def __init__(self, name, health, armor, critical_rate, attack_power):
        self.__name = name
        self.__health = health
        self.__armor = armor
        self.__critical_rate = critical_rate
        self.__attack_power = attack_power

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

    def get_critical_rate(self):
        return self.__critical_rate

    def set_critical_rate(self, critical_rate):
        self.__critical_rate = critical_rate

    def get_attack_power(self):
        return self.__attack_power

    def set_attack_power(self, attack_power):
        self.__attack_power = attack_power

    def show_info(self):
        print(f'Name:{self.__name}\nHealth: {self.__health}\nArmor:{self.__armor}\nCritical Rate:{self.__critical_rate}\nAttack Power:{self.__attack_power}')

    def special_skill(self):
        pass

    def damage(self, target):
        return self.__attack_power - target.__armor

# Player Characters
class SwordMaster(Character):
    def __init__(self, name):
        super().__init__(name, 80, 30, 1.7, 60)

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, 70, 25, 1.6, 50)

class Wizard(Character):
    def __init__(self, name):
        super().__init__(name, 50, 15, 1, 100)

class Cleric(Character):
    def __init__(self, name):
        super().__init__(name, 60, 40, 1, 70)

class Assassin(Character):
    def __init__(self, name, ):
        super().__init__(name, 75, 30, 2, 60)

class Tank(Character):
    def __init__(self, name):
        super().__init__(name, 100, 50, 1.5, 70)

class Warlock(Character):
    def __init__(self, name,):
        super().__init__(name,50, 25, 1, 80)

#--------------------

# Monster Characters
class GeneralMonster(Character):
    def __init__(self, name, health, armor, critical_rate, attack_power):
        super().__init__(name,health,armor,critical_rate,attack_power)

class UniqueMonster(Character):
    def __init__(self, name, health, armor, critical_rate, attack_power):
        super().__init__(name,health,armor,critical_rate,attack_power)
