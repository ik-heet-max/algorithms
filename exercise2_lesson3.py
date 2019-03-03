# Во втором массиве сохранить индексы четных элементов первого массива

import random

even = []
size = int(input("Enter size of array: "))
array = [random.randint(0, 100) for _ in range(size)]
print(array)

for i, item in enumerate(array):
    if item % 2 == 0:
        even.append(i)

print(even)