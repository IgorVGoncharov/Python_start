# Создайте программу для игры в ""Крестики-нолики"" (Добавьте игру против бота)

import os
import time
import random

val = ['1','2','3','4','5','6','7','8','9']

def Game(val): # игровое поле на основе списка val
    print(f" {val[0]} | {val[1]} | {val[2]}")
    print('---|---|---')
    print(f" {val[3]} | {val[4]} | {val[5]}")
    print('---|---|---')
    print(f" {val[6]} | {val[7]} | {val[8]}")

def Choice(text): #возвращает выбранны Х или О для второго игорока (текст)???????????????????7
    if FirstPlayer == "X":
        print(f"\nИгрок 1 выбрал 'X', значит {text} играет - 'O'\n")
        val = "O"
    else:
        print(f"\nИгрок 1 выбрал 'O', значит {text} играет - 'X'\n")
        val = "X"
    time.sleep(2)
    return val

def Victory(): #проверяет победил кто или нет
    vict_list = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8),(0,4,8),(6,4,2)] 
    res = 0
    for i in vict_list:
        if val[i[0]] == val[i[1]] == val[i[2]]:
            res = 2
    choiselist = ["X", "O"]
    temp = 0
    for i in val:
        if i not in choiselist:
            temp += 1
    if temp == 0:
        res = 1
    return res

def PlayerMove(Player, PlayerName): #функция хода игрока 1 или игрока 2
    num = int(input(f'"{Player}": {PlayerName} - Ваш ход: '))
    if num < 1 or num > 10:
        print('Такой клетки нет, попробуйте еще раз!')
        time.sleep(2)
        return False
    else: 
        if val[num-1] == "X" or val[num-1] == "O":
            print('Такую клетку уже выбирали, попробуйте еще раз!')
            time.sleep(2)
            return False
        else:
            val[num-1] = Player

def CompMove(value): #функция хода компютера
    choiselist = ["X", "O"]
    vict_list = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8),(0,4,8),(6,4,2)] 
    temp = True
    for i in sorted(vict_list, key=lambda a:random.random()):
        if val[i[0]] == val[i[1]] and  val[i[2]] not in choiselist:
            val[i[2]] = value
            temp = False 
            break
        elif val[i[0]] == val[i[2]] and val[i[1]] not in choiselist:
            val[i[1]] = value
            temp = False
            break
        elif val[i[1]] == val[i[2]] and val[i[0]] not in choiselist:
            val[i[0]] = value
            temp = False
            break
    if temp:
        for i in sorted(vict_list, key=lambda a:random.random()):  
            if val[i[0]] in choiselist:
                val[i[2]] = value
                break
            elif val[i[1]] in choiselist:
                val[i[2]] = value
                break
            elif val[i[2]] in choiselist:
                val[i[0]] = value
                break

def Start(game_type):
    step = 1
    while Victory() == 0:
        os.system("CLS")
        Game(val)
        print('Введите номер клетки от 1 до 9: ')
        if step == 1:
            if PlayerMove(FirstPlayer, FirstPlayerName) == False:
                step = 1
            else:
                step = 2
        else:
            if game_type == 1:
                CompMove(comp)
                step = 1
            else:
                if PlayerMove(SecPlayer, SecPlayerName) == False:
                    step = 2    
                else: 
                    step = 1
        os.system("CLS")
        Game(val)
        if Victory() == 1:
            print('Игра закончена ничьей!!!')
        else:      
            if step == 2:
                print(f"\nПоздравляем!!! {FirstPlayerName}, Вы победитель!")
            else:
                if game_type == 1:
                    print(f"\nВ это раз комрьютер Вас обыграл!") 
                else:
                    print(f"\nПоздравляем!!! {SecPlayerName}, Вы победитель!")        

while True:
    try:
        os.system("CLS")
        print('Доброе пожаловать в игру "Крестики и нолики!"\n')
        temp = True
        while temp:
            game_type = int(input("Если Вы хотите сиграть с компьютером, введите '1', если с другим пользователем - '2': "))
            if game_type < 1 or game_type > 2:
                print("\nВведено не верное число! Попробуйте еще раз.")
            else:
                temp = False
        os.system("CLS")
        if game_type == 1:
            print('Вы выбрали игру с компьютером.\n')
        else:
            print('Вы выбрали игру с другим пользователем.\n')

        FirstPlayerName = input('Игрок 1, введите свое имя: ')
        while temp == False:
            FirstPlayer = int(input("Если Вы будете играть 'X' нажмите '1'. Если 'О', нажмите '2': "))
            if FirstPlayer < 1 or FirstPlayer > 2:
                print("\nВведено не верное число! Попробуйте еще раз.")
            else:
                temp = True
                if FirstPlayer == 1:
                    FirstPlayer = "X"
                    OtherPlayer = "O"
                else:
                    FirstPlayer = "O"
                    OtherPlayer = "X"

        if game_type == 1:
            comp = Choice('компьютер')
        else:
            SecPlayerName = input('\nИгрок 2, введите свое имя: ')
            SecPlayer = Choice("игрок 2")                     

        while temp:
            Start(game_type)
            time.sleep(1)
            newgame = int(input('\nЕсли Вы хотите сыграть еще раз, нажмите "1", если нет, нажмите "0".'))
            if newgame == 1:
                val = ['1','2','3','4','5','6','7','8','9']
            else:
                temp = False
        break
    except:
        print("Ошибка ввода. Введено не число!")   