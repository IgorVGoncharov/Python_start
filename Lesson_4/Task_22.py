# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.
# Input: 11 6/
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)
# Output: 11 6
# 6 12

from random import randint

while True:
    try:
        n = int(input("Введите размерность первого списка: "))
        m = int(input("Введите размерность второго списка: "))
        def ListCreate(size):
            arr = []
            for i in range(0, size):
                arr.append(randint(1, 20))
            return arr
        if n < 1 or m < 1:
            print("В списке не может быть меньше одного элемента!")
            break
        else:
            FirstList = ListCreate(n)
            print(f"Первый список: \n {FirstList}")
            SecList = ListCreate(m)
            print(f"Второй список: \n {SecList}")
            result = sorted(set(FirstList).intersection(set(SecList)))
            if result == []:
                print("В списках нет одинаковых чисел!")
                break
            else:
                print(f"Числа, которые встречаются в обоих списках: {result}")
                break
    except:
        print("Ошибка ввода. Введено не число!")

