# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, 
# поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и 
# нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды 
# с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.
#Input: 4
#(значения сгенерированы случайным образом
#4 2 3 1 )
#Output: 9

from random import randint

while True:
    try:
        def ListCreate(size):
            arr = []
            while len(arr) < size:
                val = randint(1, size)
                if val not in arr:
                    arr.append(val)
            return arr
        n = int(input("Введите количество кустов на грядке: "))
        if n < 3:
            print("Количество грядок не может быть меньше трех.")
        else:
            BerrysCount = ListCreate(n)
            print(BerrysCount)
            max = BerrysCount[-1] + BerrysCount[0] + BerrysCount[1]
            for i in range(1, n-1):
                val = BerrysCount[i-1] + BerrysCount[i] + BerrysCount[i+1]
                if val > max:
                    max = val
            print(f"Максимальное число ягод, которjе можно собрать = {max}")
            break
    except:
        print("Ошибка ввода. Введено не число!")