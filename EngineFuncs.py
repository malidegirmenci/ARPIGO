import random

from Chars import SwordMaster, Archer, Wizard
from Helper import show_message, centered_title, show_menu, loading_bar
from Items import Weapon
from UserSystem import user

char_list = ['Kılıç Ustası', 'Okçu', 'Büyücü','Çıkış Yap']

NAME = user['name']

def fight(player, enemy):
    order = random.randint(1, 2)
    #print(order)
    round = 1
    while True:
        if enemy.get_health() <= 0 or player.get_health() <= 0:
            break
        print(centered_title(f'{round}. raunt'))
        player_damage = player.damage(enemy)
        enemy_damage = enemy.damage(player)
        if order == 1:
            if player.get_health() > 0:
                enemy.set_health(enemy.get_health() - player_damage)
                print(f'{player.get_type_of_char()} {player.get_name()}, {enemy.get_name()}e {player_damage} hasar verdi.')
                print(f'{player.get_type_of_char()} {player.get_name()} Sağlık: {player.get_health()} | {enemy.get_name()} Sağlık: {enemy.get_health()}')
                player.set_health(player.get_health() - enemy_damage)
                print(f'{enemy.get_name()}, {player.get_type_of_char()} {player.get_name()}e {enemy_damage} hasar verdi.')
                print(f'{enemy.get_name()} Sağlık: {enemy.get_health()} | {player.get_type_of_char()} {player.get_name()} Sağlık: {player.get_health()}')
        if order == 2:
            if enemy.get_health() > 0:
                player.set_health(player.get_health() - enemy_damage)
                print(f'{enemy.get_name()}, {player.get_type_of_char()} {player.get_name()}e {enemy_damage} hasar verdi.')
                print(f'{enemy.get_name()} Sağlık: {enemy.get_health()} | {player.get_type_of_char()} {player.get_name()} Sağlık: {player.get_health()}')
                enemy.set_health(enemy.get_health() - player_damage)
                print(f'{player.get_type_of_char()} {player.get_name()}, {enemy.get_name()}e {player_damage} hasar verdi.')
                print(f'{player.get_type_of_char()} {player.get_name()} Sağlık: {player.get_health()} | {enemy.get_name()} Sağlık: {enemy.get_health()}')
        round += 1
        if enemy.get_health() <= 0:
            player.set_coin(player.get_coin() + enemy.get_reward())
            show_message(f'{player.get_type_of_char()} {player.get_name()} {enemy.get_reward()} coin kazandı!')

def create_char():
    player = ''
    show_menu(char_list, 'KARAKTER SEÇİM EKRANI')
    choice_char = input('Bir karakter seçiniz : ')
    if choice_char == '1':
        player = SwordMaster(NAME)
        show_message('Kılıç ustası oluşturuldu.')
    elif choice_char == '2':
        player = Archer(NAME)
        show_message('Okçu oluşturuldu.')
    elif choice_char == '3':
        player = Wizard(NAME)
        show_message('Wizard oluşturuldu.')
    player.show_info()
    return player

def camp(player):
    player.show_info()
    show_menu(['Dinlen', 'Envantere Bak', "Gepetto'yu Ziyaret Et", 'Üst Menüye Çık'],'Kamp Alanı')
    choice = input('Yapmak istediğin eylemi seçiniz : ')
    if choice == '1':
        loading_bar()
        if player.get_type_of_char() == 'Sword Master':
            player.set_health(80)
        if player.get_type_of_char() == 'Archer':
            player.set_health(70)
        if player.get_type_of_char() == 'Wizard':
            player.set_health(50)
        show_message('Savaşçı kendine geldi canı fullendi.')
        player.show_info()
    if choice == '2':
        print(centered_title('Envanter'))
        if player.get_inventory():
            player.show_inventory()
        else:
            show_message('Envanteriniz bomboş.')
    if choice == '3':
        show_menu(['Dükkana bak', 'Görevlere bak'],'Gepetto Usta')
        choice = input('Yapmak istediğiniz eylemi seçiniz : ')
        if choice == '1':
            show_menu(['Silahlar', 'Zırhlar'], 'Dükkan')
            choice2 = input('Hangi eşyayı satın almak istiyorsunuz : ')
            if choice2 == '1':
                show_menu(['Çifte Kılıç', 'Yay', 'Asa'], 'Silahlar')
                choice3 = input('Hangi silahı almak istersiniz : ')
                if choice3 == '1':
                    dual_swords = Weapon('Dual Swords', 70, 100, 1.2)
                    player.add_item_in_inventory(dual_swords)
                if choice3 == '2':
                    bow = Weapon('Bow', 60, 100, 1.4)
                    player.add_item_in_inventory(bow)
                if choice3 == '3':
                    staff = Weapon('Staff', 70, 100, 1.2)
                    player.add_item_in_inventory(staff)