# Определить, является ли год, который ввел пользователем,
# високосным или невисокосным.

year = int(input("Enter year: "))
if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        print("The entered year is a common year")
    else:
        print("The entered year is a leap year!")
else:
    print("The entered year is a common year")