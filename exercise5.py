# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят
# и сколько между ними находится букв.

import string
first = input("Enter first character in lower case: ")
second = input("Enter second character in lower case: ")
print("First letter's position is: ", string.ascii_lowercase.index(first) + 1)
print("Second letter's position is: ", string.ascii_lowercase.index(second) + 1)
print("There are {} characters between the two letters in the alphabet".format(abs(string.ascii_lowercase.index(second) - string.ascii_lowercase.index(first)) - 1))