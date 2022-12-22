# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.
# Ввод: 5
# Ввод: 1
# 1 2 1 2 2
# Вывод: 2

import random

while True:
    try:
        len = int(input("Введите длину массива: "))
        if len <= 1:
            print("В массиве не может быть меньше 2 элементов!")
            break
        else:
            numb = int(input("Введите натуральное число: "))
            arr = []
            amount = 0
        for i in range(0 , len):
            arr.append(random.randint(1, len//2))
            if arr[i] == numb:
                amount +=1
        if amount == 0:
            print("Введенное число в массиве не найдено.")
            break
        else:
            print(f'Массив: \n {arr}')
            print(f'Число {numb} встречается в массиве: {amount}')
            break
    except:
        print("Ошибка ввода. Введено не число!")