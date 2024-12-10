from EngineFuncs import create_char, camp
from Helper import centered_title, show_menu, show_message, loading_bar
from UserSystem import login, user_menu_list, register
player = None
is_logged_in = False
while True:
    show_menu(user_menu_list, 'ARPIGO')
    choice = input('Yapmak istediğiniz eylemi seçiniz : ')
    if choice == '1':
        is_logged_in = login()
        #print(is_logged_in)
        if is_logged_in:
            if player:
                show_message(f'Hoşgeldin maceracı {player.get_name()}. Kaldığın yerden maceraya devam et.', )
            else:
                show_message('Hemen bir maceracı oluştur ve serüvene katıl.')
                player = create_char()

    elif choice == '2':
        register()
    elif choice == '3':
        show_message('Yolun açık olsun savaşçı. \nÇıkış yapılıyor.')
        loading_bar()
        break
'''
player = create_char()
show_menu(['Kamp Alanı','Kayıp Ormanlar', 'Gölge Dağı', 'Terkedilmiş Şehir', 'Orion Krallığı'],'CHAPTER 1')
choice = input('Gitmek istediğiniz yeri seçiniz: ')
print(player.get_health())
if choice == '1':
    camp(player)
elif choice == '2':
    show_message('Kayıp ormanlar')
'''

