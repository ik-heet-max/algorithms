# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число; 
# случайное вещественное число;
# случайный символ.

import string
import random

lower_int = int(input("Enter integer: "))					# случайное целое число; 
upper_int = int(input("Enter one more integer (larger than the first one): "))
print(random.randint(lower_int, upper_int))

lower_float = float(input("Enter float: "))					# случайное вещественное число;
upper_float = float(input("Enter one more (larger than the first): "))
print("%.4f" % random.uniform(lower_float, upper_float))

lower_char = input("Enter letter: ")						# случайный символ.
upper_char = input("Enter another: ")
character = list(string.ascii_lowercase)[random.randint(string.ascii_lowercase.index(lower_char), string.ascii_lowercase.index(upper_char))]
print(character)