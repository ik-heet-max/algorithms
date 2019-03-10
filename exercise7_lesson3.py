# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными),
# так и различаться.

import random

size = int(input("Enter size of array: "))
array = [random.randint(0, 100) for _ in range(size)]

minimum = array[0]
second_minimum = array[1]
for i, item in enumerate(array):
    if array[i] < minimum:
        minimum = array[i]

for i, item in enumerate(array):
    if minimum < array[i] < second_minimum:
        second_minimum = array[i]

print(array)
print(minimum)
print(second_minimum)
