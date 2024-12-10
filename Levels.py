from Chars import GeneralMonster, SwordMaster, UniqueMonster
from EngineFuncs import fight, camp
from Helper import show_story, centered_title, show_message, loading_bar
from Chars import SwordMaster
import random
player2 = SwordMaster('Kamil')
print(player2)
def lost_forests(player):
    print(centered_title('KAYIP ORMANLAR'))
    rand_monster_count = random.randint(2, 5)
    #show_story("Bir zamanlar, Kayıp Ormanlar, ışıkla dans eden peri tozları ve şarkı söyleyen ağaçlarla doluydu. \nAncak, ormanın kalbinde yaşayan Poison Ivy'nin karanlık büyüsü, burayı zehirli bir labirente çevirdi. \nKötü büyü, ormanı yalnızca cesur kahramanların geçebileceği bir yere dönüştürdü. \nOrmanın derinliklerinden gelen fısıltılar, Poison Ivy'nin eski bir tapınağı koruduğunu söylüyor. \nBu tapınağın içinde ormanın kaderini değiştirebilecek bir sır saklı olabilir.")
    manter_count_list = []
    counter = 1
    for _ in range(rand_monster_count): #5
        manter = GeneralMonster(f'{counter}.Manter', 100,65,85, 15)
        manter_count_list.append(manter)
        counter += 1
    while rand_monster_count > 0:
        if player.get_health() > 0:
            fight(player,manter_count_list[rand_monster_count - 1])
            rand_monster_count -= 1
        else:
            break
    if player.get_health() <= 0:
        show_message(f'{player.get_type_of_char()}{player.get_name()} öldü! Kampa yönlendiriliyorsunuz')
        loading_bar()
        camp(player)
    else:
        show_story(f'Manterlerin hepsini öldürdün. Poison Ivy ile karşılaşacaksın\n')
        choice = input('Poison Ivy ile karşılaşmak istiyor musun? Evet/Hayır: ')
        if choice == 'Evet' or choice == 'e':
            poison_ivy = UniqueMonster('Poison Ivy', 100, 35, 30,50, "Toxin Seed")
            fight(player, poison_ivy)
            if poison_ivy.get_health() <= 0:
                player.add_quest_items(poison_ivy.get_quest_item())
                show_message(f'{poison_ivy.get_name()} toxin seed nesnesi kazanıldı')
        else:
            show_message('Kamp alanına geri dönüyorsun')
            loading_bar()
            camp(player)

lost_forests(player2)