# Задача 8
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

m = int(input("Введите количество плиток по горизонтали: "))
n = int(input("Введите количество плиток по вертикали: "))
k = int(input("Введите количество долек, которые хотите отломить: "))
if k >= (m * n) or k < 0:
    print("Такое количество долек отломить нельзя!")
elif k % m == 0 or k % n == 0:
    print("Так отломить можно!))")
else:
    print("Так отломить нельзя")
