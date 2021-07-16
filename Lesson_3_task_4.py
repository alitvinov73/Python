# Для каждого упражнения написать программную реализацию.
# Код пишите в файлах с расширением .py в кодировке UTF-8 (в PyCharm работает по умолчанию).
# Каждую задачу необходимо сохранять в отдельный файл. Рекомендуем использовать английские имена,
# например, les_3_task_1, les_3_task_2 и т.д.
# Для оценки «Отлично» достаточно выполнить 5 любых задания на ваш выбор («Отлично» ставится за работы без ошибок).
# Например, если вы сдадите 8 заданий и 3 из них сделаны неверно, оценка не может быть отличной.

def generator_Array(lenArr=10, nStart=1, nEnd=100):
    tmpList = []
    for i in range(lenArr):
        tmpList.append(random.randint(nStart, nEnd))
    return tmpList



# 4. Определить, какое число в массиве встречается чаще всего.
import time

startTime = time.time()

print('\n4. Определить, какое число в массиве встречается чаще всего.')
list_1 = generator_Array(200)  # генерация тестового массива
list_1.sort()  # сортировка тестового массива
list_2 = []  # массив для хранения значений элементов и их повторений

for i in range(len(list_1)):
    list_2.append(list_1.count(list_1[i]))

print(f'Исходный массив {list_1}')
print(f'Число {list_1[list_2.index(max(list_2))]} встречается в массиве максимальное количество раз: {max(list_2)}.')
print(f'Время выполнения кода: {(time.time() - startTime):.15f} секунд.')

