# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента? (Добавьте игру против бота)

import random
import os

count = 2021


def PlayerMove(playername, gametype):
    global count
    temp = True
    while temp:
        if count >= 28:
            player = int(input(f'{playername}, введите значение от 1 до 28: '))
            if player < 1 or player > 28:
                print("Введено не верное значение, повторите ввод!")
                break
            else:
                temp = False
        else:
            player = int(
                input(f'{playername}, введите значение от 1 до {count}: '))
            if player < 1 or player > count:
                print("Введено не верное значение, повторите ввод!")
                break
            else:
                temp = False
        count = count - player
        print(f"Осталось конфет: {count}")


def CompMove():
    global count
    if count > 29 and count < 56:
        move = count - 29
    elif count >= 56 or count == 29:
        move = random.randint(1, 28)
    elif count < 29:
        move = count
    count = count - move
    print(f"Компьютер сделал ход: {move}")
    print(f"Осталось конфет: {count}")


def game(player_name):
    global firstPlayerName
    firstmove = random.randint(1, 2)
    if firstmove == 1:
        print(f"\n{firstPlayerName} делает первый ход!")
    else:
        print(f"\n{player_name} делает первый ход!")

    step = firstmove

    while count > 0:
        if step == 1:
            PlayerMove(firstPlayerName, gametype)
            step = 2
        else:
            if player_name == 'Компьютер':
                CompMove()
            else:
                PlayerMove(player_name, gametype)
            step = 1

    if step == 2:
        print(f"{firstPlayerName} - ты победитель!")
    else:
        print(f"{player_name} - ты победитель!")


os.system("CLS")

gametype = int(input(
    'Выберите режим игры: если хотите играть с компьютером, нажмите "1", с другим игроком - "2": '))

os.system("CLS")
firstPlayerName = input('Игрок 1, введите свое имя: ')
if gametype == 2:
    SecPlayerName = input('Игрок 2, введите свое имя: ')

if gametype == 1:
    game('Компьютер')
else:
    game(SecPlayerName)
