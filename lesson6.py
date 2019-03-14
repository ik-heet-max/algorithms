# Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47)
# [MSC v.1914 32 bit (Intel)] on win32
# 64-разрядная ОС

# Подсчитать, сколько было выделено памяти под переменные
# в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы
# с наиболее эффективным использованием памяти.

import sys
import random


def show_size_(x):
    size = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size_(value)
                size += show_size_(value)
        elif not isinstance(x, str):
            for term in x:
                show_size_(term)
                size += show_size_(term)
    return size

# 1.
# Берем неизменный код из д/з

rows = int(input("Enter number of rows: "))
columns = int(input("Enter numbers of columns: "))

array = [[random.randint(1, 100) for _ in range(columns)] for _ in range(rows)]
for line in array:
    print(line)

minima = []
for j in range(len(array[0])):
    min_in_col = array[0][j]
    for i, item in enumerate(array):
        if array[i][j] < min_in_col:
            min_in_col = array[i][j]
    minima.append(min_in_col)

largest_minimum = minima[0]
for i, item in enumerate(minima):
    if minima[i] > largest_minimum:
        largest_minimum = minima[i]

print(show_size_(array))
print(show_size_(tuple(array)))
print(show_size_(minima))
print(show_size_(tuple(minima)))


# 6336 - столько байт занимает матрица 15х20 в виде списка из списков
# 6308 - столько байт она занимает в виде кортежа из списков
# 310 - столько байт занимает список из 15 целых чисел
# 298 - столько - кортеж с 15 целыми числами

#2.
rows = int(input("Enter number of rows: "))
columns = int(input("Enter numbers of columns: "))

array = [tuple([random.randint(1, 100) for _ in range(columns)]) for _ in range(rows)] # здесь представили строки будущей матрицы
for line in array:																		# в виде кортежей с целыми числами
    print(line)

minima = []
for j in range(len(array[0])):
    min_in_col = array[0][j]
    for i, item in enumerate(array):
        if array[i][j] < min_in_col:
            min_in_col = array[i][j]
    minima.append(min_in_col)

largest_minimum = minima[0]
for i, item in enumerate(minima):
    if minima[i] > largest_minimum:
        largest_minimum = minima[i]

print(show_size_(array))
print(show_size_(tuple(array)))


# 6096 (против 6336) - столько байт занимает матрица 15х20 в виде списка из кортежей
# 6068 (против 6308) - столько байт она занимает в виде кортежа из кортежей (надеюсь, так говорить не неграмотно)

# Видно, что использование кортежей позволяет сократить объем памяти, используемой программой