import time
import keyboard
import random

start = ''
restart = 0

def game():
    w = '■'
    p = ' '
    map = [[w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
           [w, p, p, p, p, p, p, p, p, p, p, p, p, p, w],
           [w, p, p, p, p, p, p, p, p, p, p, p, p, p, w],
           [w, p, p, p, p, p, p, p, p, p, p, p, p, p, w],
           [w, p, p, p, p, p, p, p, p, p, p, p, p, p, w],
           [w, p, p, p, p, p, p, p, p, p, p, p, p, p, w],
           [w, p, p, p, p, p, p, p, p, p, p, p, p, p, w],
           [w, p, p, p, p, p, p, p, p, p, p, p, p, p, w],
           [w, p, p, p, p, p, p, p, p, p, p, p, p, p, w],
           [w, p, p, p, p, p, p, p, p, p, p, p, p, p, w],
           [w, p, p, p, p, p, p, p, p, p, p, p, p, p, w],
           [w, p, p, p, p, p, p, p, p, p, p, p, p, p, w],
           [w, p, p, p, p, p, p, p, p, p, p, p, p, p, w],
           [w, p, p, p, p, p, p, p, p, p, p, p, p, p, w],
           [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w]]

    you_lose = '''╔╗  ╔╗╔═══╗╔╗ ╔╗     ╔╗   ╔═══╗╔═══╗╔═══╗
║╚╗╔╝║║╔═╗║║║ ║║     ║║   ║╔═╗║║╔═╗║║╔══╝
╚╗╚╝╔╝║║ ║║║║ ║║     ║║   ║║ ║║║╚══╗║╚══╗
 ╚╗╔╝ ║║ ║║║║ ║║     ║║ ╔╗║║ ║║╚══╗║║╔══╝
  ║║  ║╚═╝║║╚═╝║     ║╚═╝║║╚═╝║║╚═╝║║╚══╗
  ╚╝  ╚═══╝╚═══╝     ╚═══╝╚═══╝╚═══╝╚═══╝'''

    difficulty = int(input('''Выберете уровень сложности:
    1 - EASY,
    2 - NORMAL,
    3 - HARD
    '''))
    while difficulty > 3:
        print('Неверно введён уровень сложности!')
        difficulty = int(input('''Выберете уровень сложности:
    1 - EASY,
    2 - NORMAL,
    3 - HARD
    '''))
    snake_siments = [[0, 1], [1, 1], [2, 1]]
    kl = 'd'
    sp = []
    v = ()
    for i in range(1, 14):
        for j in range(1, 14):
            v = (i, j)
            sp.append(v)
    zn = [x for x in sp if x not in snake_siments]
    applex, appley = random.choice(zn)

    while True:
        num = snake_siments[0]
        prx, pry = snake_siments[-1]
        for i in range(1, len(snake_siments)):
            snake_siments[i - 1] = snake_siments[i]
        if kl == 'd':
            prx += 1
            snake_siments[-1] = prx, pry
        elif kl == 'a':
            prx -= 1
            snake_siments[-1] = prx, pry
        elif kl == 'w':
            pry -= 1
            snake_siments[-1] = prx, pry
        elif kl == 's':
            pry += 1
            snake_siments[-1] = prx, pry

        x1, y1 = snake_siments[-1]
        if x1 == 0 or x1 == 14 or y1 == 0 or y1 == 14:
            print()
            print(you_lose)
            break
        if len(snake_siments) == 169:
            print()
            print('''██╗   ██╗ █████╗ ██╗   ██╗         ██╗       ██╗██╗███╗  ██╗
            ╚██╗ ██╔╝██╔══██╗██║   ██║         ██║  ██╗  ██║██║████╗ ██║
             ╚████╔╝ ██║  ██║██║   ██║         ╚██╗████╗██╔╝██║██╔██╗██║
              ╚██╔╝  ██║  ██║██║   ██║          ████╔═████║ ██║██║╚████║
               ██║   ╚█████╔╝╚██████╔╝          ╚██╔╝ ╚██╔╝ ██║██║ ╚███║
               ╚═╝    ╚════╝  ╚═════╝            ╚═╝   ╚═╝  ╚═╝╚═╝  ╚══╝''')

        if prx == applex and pry == appley:
            map[appley][applex] = p
            zn = [x for x in sp if x not in snake_siments]
            applex, appley = random.choice(zn)
            snake_siments.insert(0, num)

        for sx, sy in snake_siments:
            map[sy][sx] = "@"
            map[appley][applex] = '●'
        print()
        for row in map:
            for element in row:
                print(element + ' ', end=' ')
            print()

        for sx, sy in snake_siments:
            map[sy][sx] = p
        time.sleep(1 / difficulty)

        if snake_siments[-1] in snake_siments[1:len(snake_siments) - 1]:
            print()
            print(you_lose)
            break

        if keyboard.is_pressed('a'):
            if kl == 'd':
                print()
                print(you_lose)
                break
            else:
                kl = 'a'
        elif keyboard.is_pressed('w'):
            if kl == 's':
                print()
                print(you_lose)
                break
            else:
                kl = 'w'
        elif keyboard.is_pressed('s'):
            if kl == 'w':
                print()
                print(you_lose)
                break
            else:
                kl = 's'
        elif keyboard.is_pressed('d'):
            if kl == 'a':
                print()
                print(you_lose)
                break
            else:
                kl = 'd'

while True:
    if restart == 0:
        start = input('''Хотите ли вы начать игру?
    'Y' - Да             'N' - Нет
     ''')
        restart = 1
    else:
        print()
        start = input('''Хотите ли вы попробовать снова?
    'Y' - Да             'N' - Нет
     ''')
    if start == 'Y' or start == 'y':
        game()
    elif start == 'N' or start == 'n':
        print()
        break
    else:
        print()
        print('НЕВЕРНО ЗАДАН ПАРАМЕТР!')