from Helper import show_message, centered_title, loading_bar

user_menu_list = ['Giriş Yap', 'Kayıt Ol', 'Çıkış Yap']

user = {'username': 'kamil16', 'password': '1234', 'name':'Kamil', 'chars':[]}
is_login = False
def login():
    print(centered_title('Giriş Yap'))
    global is_login
    if is_login:
        show_message('Kullanıcı zaten giriş yaptı')
    else:
        username = input('Kullanıcı Adı : ')
        password = input('Parola : ')
        if username == user['username'] and password == user['password']:
            show_message(f'Hoş geldin, {user['name']}')
            show_message('Oyuna giriş yapıldı. Yönlendiriliyorsunuz. ')
            loading_bar()
            return True
        else:
            show_message('Kullanıcı bilgileri yanlış, tekrar deneyiniz.')
            loading_bar()
            return False

def register():
    print(centered_title('Kayıt Ol'))
    global user
    username = input('Kullanıcı Adı : ')
    password = input('Parola : ')
    name = input('İsim: ')
    user = {'username': username, 'password': password, 'name': name}
    show_message('Kayıt oluşturuldu. Ana menüye yönlendiriliyorsunuz.')
    loading_bar()