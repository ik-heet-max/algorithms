# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

rows = int(input("Enter number of rows: "))
columns = int(input("Enter numbers of columns: "))

array = [[random.randint(1, 100) for _ in range(columns)] for _ in range(rows)]
for line in array:
    print(line)

minima = []
for j, item_ in enumerate(line): # здесь питон попытался ругнуться на слово line,
    min_in_col = array[0][j]		#  но по-другому я не смог придумать
    for i, item in enumerate(array):
        if array[i][j] < min_in_col:
            min_in_col = array[i][j]
    minima.append(min_in_col)
print("These are the smallest items in each column:", minima)

largest_minimum = minima[0]
for i, item in enumerate(minima):
    if minima[i] > largest_minimum:
        largest_minimum = minima[i]

print("The largest minimum among them is", largest_minimum)
