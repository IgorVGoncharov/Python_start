# Задача 102 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def SimleFactorList(n):
    # создание списка из простых чисел
    lst = []
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    # поиск простых множителей числа
    newlist = []
    for i in lst:
        while n % i == 0:
            n = n/i
            newlist.append(i)
    return newlist

while True:
    try:
        n = int(input("Введите натуральное число: "))
        if n < 1:
            print("Введено не натуральное число!")
        else:
            print(f'Список простых множителей числа {n} = {SimleFactorList(n)}')
            break
    except:
        print("Ошибка ввода. Введено не число!")