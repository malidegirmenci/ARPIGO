class Weapon:
    def __init__(self, name, attack_power,  durability, critical_rate):
        self.__name = name
        self.__attack_power = attack_power
        self.__durability = durability
        self.__critical_rate = critical_rate

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

    def show_weapon(self):
        print(f'Name: {self.__name} Attack Power: {self.__attack_power}, Durability: {self.__durability}, Critical Rate: {self.__critical_rate}')

class Armor:
    def __init__(self, name, defence, durability, block_rate):
        self.__name = name
        self.__defence = defence
        self.__durability = durability
        self.__block_rate = block_rate

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

    def show_armor(self):
        print(f'Name: {self.__name} Defence: {self.__defence}, Durability: {self.__durability}, Block Rate: {self.__block_rate}')
