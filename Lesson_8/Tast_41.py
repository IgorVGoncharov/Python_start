def transform(text): #исправляет неточности ввода
    text = text.replace(' ', "")
    text = text.replace('+', " + ")
    text = text.replace('-', " - ")
    text = text.replace('*', " * ")
    text = text.replace('/', " / ")
    text = text.replace('(', " ( ")
    text = text.replace(')', " ) ")
    return text.split()

def SimpleCalc(a, b, c): #вычисляет выражение из 2 чисел
    if c == '+':
        return int(a) + int(b)
    elif c == '-':  
        return int(a) - int(b)
    elif c == '*':
        return int(a) * int(b)
    elif c == '/':
        return int(int(a) / int(b))
    else:
        print('Ошибка выражения')

def MultiCulc(text): #вычисляет выражение их множетсва чисел без приоритета
    result = SimpleCalc(text[0], text[2], text[1])
    for i in range(3, len(text) - 1, 2):
        result = SimpleCalc(result, text[i+1], text[i])
    return result

def PrioritetCalc(text): #вычисляет выражение их множетсва чисел с приоритетом
    new_list = []
    res = text[0]
    for i in range(1, len(text) - 1, 2):
        if text[i] == '*' or text[i] == '/':
            res = SimpleCalc(text[i-1], text[i+1], text[i])
            if i == len(text) - 2:
                new_list.append(res)
        else:
            new_list.append(res)
            new_list.append(text[i])
            res = text[i+1]
            if i == len(text)-2:
                new_list.append(text[-1])
    if len(new_list) == 1:
        return int(new_list[0])
    else:
        return MultiCulc(new_list)


text_for_calc = '4 * 2 + 6 + 25 / 5 - 10' #выражение для калькулятора по приоритету 
result = PrioritetCalc(transform(text_for_calc))
print(f"Результат вычислений без учета скобок равен = {result}")
