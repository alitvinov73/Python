# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
num = int(input('Введите число элементов: '))
print(sum([(-0.5) ** i for i in range(0, num)]))