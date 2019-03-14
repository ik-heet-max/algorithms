import random


def median(array):
    for i in range(len(array)):
        less_than = 0
        more_than = 0
        for j in range(len(array)):
            if i != j:
                if array[i] < array[j]:
                    less_than += 1
                elif array[i] > array[j]:
                    more_than += 1
            else:
                continue
        if less_than == more_than:
            return array[i]


m = int(input("Enter m: "))
my_array = [random.randint(-100, 100) for _ in range(2 * m + 1)]
print(my_array)
print(median(my_array))
