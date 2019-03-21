# В массиве случайных целых чисел поменять местами
# минимальный и максимальный элементы.

import random

size = int(input("Enter size of array: "))
array = [random.randint(0, 100) for _ in range(size)]
print(array)

min_item = array[0]
max_item = array[1]

for i, item in enumerate(array):
    if item < min_item:
        min_item = item
    if item > max_item:
        max_item = item

i_min = [i for i, item in enumerate(array) if item == min_item]
i_max = [i for i, item in enumerate(array) if item == max_item]

for i in i_min:
    array[i] = max_item
for i in i_max:
    array[i] = min_item

print(min_item)
print(max_item)

print("Extrema swapped: ", array)
