
def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(','))
    return result

def save_data_to_file(name, data_list):
    with open(name, 'a', encoding='utf8') as datafile:
        datafile.writelines('\n' + str(data_list))

def PrintBus():
    data = read_data_from_file('C:/GeekBrains/Python/Lesson_7/bus.txt')
    print("Список автобусов: \n")
    for i in data:
        print(f'Автобус: {i[0]}\tНомер: {i[1]}\n')

def AddBus():
    print("Добавление автобуса: \n")
    bus = input('Введите автобус: ')
    num = input("Введите номер автобуса: ")
    new_bus = bus + ', ' + num
    save_data_to_file('C:/GeekBrains/Python/Lesson_7/bus.txt', new_bus)

def PrintDriver():
    data = read_data_from_file('C:/GeekBrains/Python/Lesson_7/driver.txt')
    print("Список водителей: \n")
    for i in data:
        print(f'Водитель: {i[0]}\tФамилия: {i[1]}\n')

def AddDriver():
    print("Добавление водителя: \n")
    driver = input('Введите водителя: ')
    name = input("Введите фамилию: ")
    new_driver = driver + ', ' + name
    save_data_to_file('C:/GeekBrains/Python/Lesson_7/driver.txt', new_driver)

def PrintRoute():
    data = read_data_from_file('C:/GeekBrains/Python/Lesson_7/marsrut.txt')
    print("Список маршрутов: \n")
    for i in data:
        print(f'Название: {i[0]}\tНомер: {i[1]}\tАвтобус: {i[2]}, Водитель: {i[3]}')

def AddRoute():
    print("Добавление маршрута: \n")
    name = input('Введите название: ')
    numb = input("Введите номер: ")
    bus = input('Введите автобус: ')
    driver = input('Введите водителя: ')
    new_route = name + ', ' + numb + ', ' + bus  + ', ' + driver
    save_data_to_file('C:/GeekBrains/Python/Lesson_7/marsrut.txt', new_route)
    
def decode():
    print('\nРасшифровка маршрута: ')
    num = 1
    route = read_data_from_file('C:/GeekBrains/Python/Lesson_7/marsrut.txt')
    driver = read_data_from_file('C:/GeekBrains/Python/Lesson_7/driver.txt')
    bus = read_data_from_file('C:/GeekBrains/Python/Lesson_7/bus.txt')
    for i in route:
        print(f'\nМаршрут {num}:')
        print(f'Название маршрута => {i[0]}\nНомер => {i[1]}')
        for j in bus:
            if i[2] == (' ' + j[0]):
                print(f'Автобус => {i[2]}\nНомер автобуса => {j[1]}')
        for h in driver:
            if i[3] == (' ' + h[0]):
                print(f'Водитель => {i[3]}\nФамилия водителя => {h[1]}')
        num += 1

