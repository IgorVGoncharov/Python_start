# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def exponent(a, b):
    if b == 0:
        return 1
    else:
        if b > 0:
            return a * exponent(a, b-1)
        else:
            return 1 / a * exponent(a, b+1)


while True:
    try:
        a = int(input("Введите число А: "))
        b = int(input("Введите число B: "))
        print(f"число {a} возведенное в степень {b} = {exponent(a, b)}")
        break
    except:
        print("Ошибка ввода. Введено не число!")
