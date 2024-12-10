class Weapon:
    def __init__(self, name, attack_power,  durability, critical_rate):
        self.__type_of_item = 'weapon'
        self.__name = name
        self.__attack_power = attack_power
        self.__durability = durability
        self.__critical_rate = critical_rate
        self.__is_equipped = False

    def get_name(self):
        return self.__name

    def get_attack_power(self):
        return self.__attack_power

    def set_attack_power(self, attack_power):
        self.__attack_power = attack_power

    def get_durability(self):
        return self.__durability

    def set_durability(self, durability):
        self.__durability = durability

    def get_critical_rate(self):
        return self.__critical_rate

    def set_critical_rate(self, critical_rate):
        self.__critical_rate = critical_rate

    def get_is_equipped(self):
        return self.__is_equipped

    def set_is_equipped(self, is_equipped):
        self.__is_equipped = is_equipped

    def get_type_of_item(self):
        return self.__type_of_item

    def show_weapon(self):
        print('WEAPON')
        print(f'Class: {self.__name}\nAttack Power: {self.__attack_power}\nDurability: {self.__durability}\nCritical Rate: {self.__critical_rate}')

hands = Weapon('Hands',1,100,1)

class Armor:
    def __init__(self, name, defence, durability, block_rate):
        self.__type_of_item = 'armor'
        self.__name = name
        self.__defence = defence
        self.__durability = durability
        self.__block_rate = block_rate
        self.__is_equipped = False

    def get_name(self):
        return self.__name

    def get_defence(self):
        return self.__defence

    def set_defence(self, defence):
        self.__defence = defence

    def get_durability(self):
        return self.__durability

    def set_durability(self, durability):
        self.__durability = durability

    def get_block_rate(self):
        return self.__block_rate

    def set_block_rate(self, block_rate):
        self.__block_rate = block_rate

    def get_is_equipped(self):
        return self.__is_equipped

    def set_is_equipped(self, is_equipped):
        self.__is_equipped = is_equipped

    def get_type_of_item(self):
        return self.__type_of_item

    def show_armor(self):
        print(f'ARMOR')
        print(f'Class:{self.__name}\nDefence: {self.__defence}\nDurability: {self.__durability}\nBlock Rate: {self.__block_rate}')

basic_armor = Armor('Basic Armor', 1, 100, 1)