import random


def merge(left, right):
    sorted_list = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            sorted_list.append(left[0])
            left.remove(left[0])
        else:
            sorted_list.append(right[0])
            right.remove(right[0])
    if len(left) == 0:
        sorted_list += right
    if len(right) == 0:
        sorted_list += left
    return sorted_list


def parse(array):
    if len(array) == 0 or len(array) == 1:
        return array
    left = parse(array[:(len(array))//2])
    right = parse(array[(len(array))//2:])
    return merge(left, right)


my_array = [float("%.2f" % random.uniform(0, 49)) for _ in range(15)]
print(my_array)
print(parse(my_array))
