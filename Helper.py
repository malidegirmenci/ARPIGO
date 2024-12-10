import time

def loading_bar():
    loading_chars = '#' * 25
    for ch in loading_chars:
        print(ch, end='')
        time.sleep(0.2)
    print('')

def show_story(story):
    for letter in story:
        print(letter, end='')
        time.sleep(0.1)

def centered_title(title, width=50):
    if len(title) >= width:
        return title[:width]
    else:
        padding = (width - len(title)) // 2
        return padding * '-' + f'| {title} |' + padding * '-'

def show_menu(menu, name_of_menu):
    title = centered_title(name_of_menu)
    print(title)
    row = 1
    for menuRow in menu:
        print(f'{row}. {menuRow}')
        row += 1
    print('-' * len(title))

def show_message(message):
    print('-'*54)
    print(message)
    print('-'*54)