# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


while True:
    try:
        n = int(input('Введите число N: '))
        val = 2
        array = []
        if n < 2:
            print("N меньше чем 2, нечего выводить!")
            break
        else:
            while val <= n:
                array.append(val)
                val *= 2
            print(array)
            break
    except:
        print("Ошибка ввода. Введено не число!")
