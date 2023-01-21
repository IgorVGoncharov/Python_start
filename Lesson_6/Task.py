import os


def MainMenu():  # основное меню
    os.system("CLS")
    while True:
        try:
            print("Добро пожаловать в телефонный справочник!!! \n")
            selection = int(input("Вот возможные варианты действий:\n\
            1 - Показать все записи \n\
            2 - Найти запись по вхождению частей имени \n\
            3 - Найти запись по телефону \n\
            4 - Добавить новый контакт \n\
            5 - Удалить контакт \n\
            6 - Изменить номер телефона у контакта \n\
            7 - Выход \n\
            Введите номер действия: "))
            if selection < 1 or selection > 7:
                print("\nТакого номера действия нет! Попробуйте еще раз.\n")
            else:
                return selection
        except:
            print("\nОшибка ввода. Введено не число!\n")


def SelectMenu():  # функция возврата в основное меню
    while True:
        try:
            temp = True
            while temp:
                val = int(input(
                    '\nВведите 1 для возврата в основное меню, 2 - для выхода из справочника: '))
                if val == 1:
                    temp = False
                    Main()
                elif val == 2:
                    break
                else:
                    print("Введено не верное значение")
            break
        except:
            print("Ошибка ввода. Введено не число!")


def ShowFile(file):  # выводит список контактов
    os.system("CLS")
    i = 1
    for j in file:
        if j == ['End', 'of', 'dict', '!']:
            pass
        else:
            print(f'Контакт №{i}:')
            print(
                f"Фамилия:\t{j[0]} \nИмя:\t\t{j[1]} \nОтчество:\t{j[2]} \nТелефон:\t{j[3]}")
            i += 1


def SearchingByName(file):  # поиск контакта по части имени
    os.system("CLS")
    temp = False
    val = input(
        'Введите имя, фимилию или отчество для поиска контакта: ').lower()
    for i in file:
        if val == str(i[0]).lower() or val == str(i[1]).lower() or val == str(i[2]).lower():
            print("\nНайденный контакт:\n")
            print(
                f"Фамилия:\t{i[0]} \nИмя:\t\t{i[1]} \nОтчество:\t{i[2]} \nТелефон:\t{i[3]}")
            temp = True
    if not temp:
        print("Значение не найдено!")


def SearchingByTel(file):  # поиск по телефону
    os.system("CLS")
    temp = False
    val = input('Введите номер телефона для поиска: ')
    for i in file:
        if (val + '\n') in i[3]:
            print("\nНайденный контакт:\n")
            print(
                f"Фамилия:\t{i[0]} \nИмя:\t\t{i[1]} \nОтчество:\t{i[2]} \nТелефон:\t{i[3]}")
            temp = True
    if not temp:
        print("Значение не найдено!")


def AddNewContact(file_data):  # добавление нового контакта
    os.system("CLS")
    new_contact = []
    print("Добавление нового контакта.\n")
    new_contact.append(input("Введите фамилию: "))
    new_contact.append(input("Введите имя: "))
    new_contact.append(input("Введите отчество: "))
    new_contact.append(input("Введите номер телефона: ") + "\n")
    file_data.insert(0, new_contact)


def DelContact(file_data):  # удаление контака
    os.system("CLS")
    temp_val = False
    print("Удаление контакта.")
    val = input('\nВведите данные контакта для поиска: ').lower()
    for i in file_data:
        if val in str(i).lower():
            print("\nНайденный контакт:\n")
            print(
                f"Фамилия:\t{i[0]} \nИмя:\t\t{i[1]} \nОтчество:\t{i[2]} \nТелефон:\t{i[3]}")
            temp = int(
                input("\nЕсли Вы хотите удалить этот контакт, нажмите - '1', если нет - '2': "))
            temp_val = True
            if temp == 1:
                file_data.remove(i)
                print('Контакт удален!')
    if not temp_val:
        print("Значение не найдено!")

    return file_data


def WriteFile(file_name, file_data):  # перезапись файда новыми данными
    with open(file_name, 'w') as data:
        for i in file_data:
            val = i[0] + ' ' + i[1] + ' ' + i[2] + ' ' + i[3]
            data.writelines(val)


def ReadFile(file_name):  # читает данные с файла
    result = []
    with open(file_name, 'r+') as data:
        for line in data:
            result.append(line.split(' '))
    return result


def ChangeContact(file):  # изменение номера телефона
    os.system("CLS")
    temp_val = False
    print("Изменение номера телефона контакта.\n")
    val = input('Введите данные контакта для поиска: ').lower()
    for i in file:
        if val in str(i).lower():
            print("\nНайденный контакт:\n")
            print(
                f"Фамилия:\t{i[0]} \nИмя:\t\t{i[1]} \nОтчество:\t{i[2]} \nТелефон:\t{i[3]}")
            temp = int(
                input('Если вы хотите изменить этот контакт, нажмите "1", если нет - "2": '))
            if temp == 1:
                tel = input('\nВведите новый номер телефона: ')
                i[3] = tel + '\n'
                temp_val = True
                print("\nНомер телефона изменен!")
                break
            elif temp == 2:
                pass
            else:
                print('Введено не верно значение!')
    if not temp_val:
        print("Значение не найдено!")
    return file


def Main():
    file_data = ReadFile('directory.txt')
    selection = MainMenu()
    if selection == 1:
        ShowFile(file_data)
        SelectMenu()
    elif selection == 2:
        SearchingByName(file_data)
        SelectMenu()
    elif selection == 3:
        SearchingByTel(file_data)
        SelectMenu()
    elif selection == 4:
        AddNewContact(file_data)
        WriteFile('directory.txt', file_data)
        SelectMenu()
    elif selection == 5:
        DelContact(file_data)
        WriteFile('directory.txt', file_data)
        SelectMenu()
    elif selection == 6:
        ChangeContact(file_data)
        WriteFile('directory.txt', file_data)
        SelectMenu()
    elif selection == 7:
        print('\nДо скорых встреч!')


Main()
