# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input("Введите текст: ")
newtext = text.split(' ')
for i in newtext:
    if 'абв' in i:
        newtext.remove(i)
print(f'Тест без слов, содержащих "абв": {" ".join(newtext)}')
        


