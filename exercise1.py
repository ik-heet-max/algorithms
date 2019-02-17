# Найти сумму и произведение цифр трехзначного числа,
# которое вводит пользователь.

number = input("Enter number: ")
summe = 0
produkt = 1
for i in number:
    summe += int(i)
    produkt *= int(i)
print(summe)
print(produkt)