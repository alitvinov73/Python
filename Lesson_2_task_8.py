# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

count = int(input('Введите количество вводимых чисел: '))
num = input('Введите цифру, которую необходимо посчитать: ')
str_1 = ''
for i in range(count):
    str_1 += input('Введите число: ')

print(f'Число {num} встречается {str_1.count(num)} раз.')