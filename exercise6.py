# Пользователь вводит номер буквы в алфавите.
# Определить, какая это буква.

import string

pos = int(input("Enter number: "))
character = list(string.ascii_lowercase)[pos - 1]
print(character)