# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки
# и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

print("Enter array's elements:\n")
matrix = [[0] * 4 for _ in range(5)]

for i in range(5):
    for j in range(3):
        matrix[i][j] = int(input("Enter element {}{}: ".format(i, j)))
        matrix[i][3] += matrix[i][j]

for line in matrix:
    print(line)
