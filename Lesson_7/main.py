import functions as fn
import os

def ReturnToMenu():
    while True:
        try:
            sel = int(input("\n* Если хоите вернуться в основное меню - '1'\n* Выйти - '2': "))
            if sel == 1:
                main()
            elif sel == 2:
                print('До новых встреч!')
                break
            elif sel != 1 or sel != 2:
                print('Введено не верное число')
            else:
                continue
            break
        except:
            print("\nОшибка ввода. Введено не число!\n")

def decoding():
    while True:
        try:   
            sel = int(input('\n* Если хотите посмотреть расшифровку маршрута, нажмите 1\n\
* Если хоите вернуться в основное меню нажмите 2\n\
* Выйти - 3\n\
Введите значение: '))
            if sel == 2:
                main()
            elif sel == 3:
                print('До новых встреч!')
                break
            elif sel == 1:
                fn.decode()
            elif sel != 1 or sel != 2 or sel != 3:
                print('Введено не верное число')
            else:
                continue
            break
        except:
            print("\nОшибка ввода. Введено не число!\n")

def main():
    os.system('cls')
    selection = int(input("1. Вывод автобусов\n\
2. Добавление автобуса\n\
3. Вывод водителя\n\
4. Добавление водителей\n\
5. Вывод маршрута\n\
6. Добавление маршрута\n\
7. Выход\n\
    \nВведите значение: "))
    if selection == 1:
        os.system('cls')
        fn.PrintBus()
        ReturnToMenu()
    elif selection == 2:
        os.system('cls')
        fn.AddBus()
        ReturnToMenu()
    elif selection == 3:
        os.system('cls')
        fn.PrintDriver()
        ReturnToMenu()
    elif selection == 4:
        os.system('cls')
        fn.AddDriver()
        ReturnToMenu()
    elif selection == 5:
        os.system('cls')
        fn.PrintRoute()
        decoding()
        ReturnToMenu()
    elif selection == 6:
        os.system('cls')
        fn.AddRoute()
        ReturnToMenu()
    elif selection == 7:
        print('До новых встреч!')
    else:
        print('Введено не верное значение!')
    
main()