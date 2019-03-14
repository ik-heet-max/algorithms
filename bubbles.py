# Вместо умного алгоритма получился лишь еще более глупый,
# который вычисляет, но в подарок идет ошибка,
# поэтому здесь почти без изменений


import random


def bubble(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    return array


my_array = [random.randint(-100, 99) for _ in range(10)]
print(my_array)
print(bubble(my_array))
