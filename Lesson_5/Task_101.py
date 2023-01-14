# Задача 101 Вычислить число π c заданной точностью d
# Пример: 
# при d = 0.001, π = 3.141    0.1 ≤ d ≤ 0.00000000001

import math

while True:
    try:
        d = (input('Введите желаемую точность числа Пи: '))
        val = sorted(set(d))
        if float(d) > 0.1 or float(d) < 0.00000000001:
            print("Введите точность в пределах: 0.1 ≤ d ≤ 0.00000000001")
        elif len(val) > 3 or int(val[2]) != 1:
            print("Введена не корректная точность. Введите другое значение.") 
        else:
            pi = str(math.pi)
            accur = len(str(d))
            print(f"Число Пи с точностью {d} = {pi[:accur]}")
            break
    except:
        print("Ошибка ввода. Введено не число!")