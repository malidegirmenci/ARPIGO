from Chars import Tank, Character, GeneralMonster, UniqueMonster, SwordMaster, Archer
from Helper import show_message
from Items import Weapon

print('!!!ARPIGO!!!')
print('New Generation RPG Game')
'''
manter = GeneralMonster('Manter', 100, 40,  60)
manter.show_info()

poisonIvy = UniqueMonster('Poison Ivy', 250, 60, 100)
poisonIvy.show_info()

player = SwordMaster('Mahmut')
player.show_info()

#player2 = Archer('Nedife', 70, 25,1.6, 50)
player2 = Archer('Nedife')
player2.show_info()

print(player2.damage(manter))

show_message(f'{player2.get_name()}, {manter.get_name()} {player2.damage(manter)} hasar verdi. ')
'''

clericRod = Weapon('Cleric Rod', 120, 100, 2)
swordMaster = SwordMaster('Kamil')
swordMaster.show_info()
swordMaster.get_weapon().show_weapon()

swordMaster.set_weapon(clericRod)
swordMaster.show_info()


