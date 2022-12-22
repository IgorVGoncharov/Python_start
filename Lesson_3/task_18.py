# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.
# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

import random

while True:
    try:
        len = int(input("Введите длину массива: "))
        if len <= 1:
            print("В массиве не может быть меньше 2 элементов!")
            break        
        else:
            arr = []
            for i in range(0 , len):
                arr.append(random.randint(1, len))
            print(f"Массив: \n {arr}")
            x = int(input("Введите число: "))
            if x < sorted(arr)[0]:
                res = sorted(arr)[0]
            elif x > sorted(arr)[-1]:
                res = sorted(arr)[-1]
            else:
                for i in range(0, len):
                    if x < sorted(arr)[i]:
                        pass
                    else:
                        if x == sorted(arr)[i]:
                            res = sorted(arr)[i]
                        else:
                            if sorted(arr)[i] - x >= x - sorted(arr)[i-1]:
                                res = sorted(arr)[i-1]
                            else:
                                res = sorted(arr)[i]
        print(f'Наиболее приближенное к {x} число = {res}')
        break        
    except:
        print("Ошибка ввода. Введено не число!")
