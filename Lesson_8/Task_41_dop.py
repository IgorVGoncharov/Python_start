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

def LastCalc(text): #вычисляет вырожения со скобками
    index_r = ''
    for i in range(0, len(text)):
        if text[i] == '(':
            index_l = i
    for i in range(0, len(text)):   
        if text[i] == ')':
            if i > index_l:   
                if index_r == '':
                    index_r = i
    midle_part = MultiCulc(transform(('').join(text[index_l+1:index_r])))
    if index_l == '0':
        left_part = ''
    else:    
        left_part = ('').join(text[:index_l])
    if index_r == len(text) + 1:
        right_part = ""
    else:   
        right_part = ('').join(text[index_r+1:])
    #print(left_part + str(midle_part) + right_part)
    return left_part + str(midle_part) + right_part

              
text_f_calc = '(10-5)*2+3*(3-1)+2' #выражение для калькулятора по приоритету с учетом скобок

result = LastCalc(transform(text_f_calc))
while True:
    if '(' in result:
        result = LastCalc(transform(result))   
    else:
        break
    
print(f'Результат вычислений c учетом скобок равен = {PrioritetCalc(transform(result))}')