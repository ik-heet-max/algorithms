# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны любому из чисел в диапазоне от 2 до 9.

divide_two = 0
divide_three = 0
divide_five = 0
divide_seven = 0

for num in range(2, 100):
    if num % 2 == 0:
        divide_two += 1
    if num % 3 == 0:
        divide_three += 1
    if num % 5 == 0:
        divide_five += 1
    if num % 7 == 0:
        divide_seven += 1

print(divide_two, "number(s) divisible by two")
print(divide_three, "number(s) divisible by three")
print(divide_two // 2, "number(s) divisible by four")
print(divide_five, "number(s) divisible by five")
print(divide_two // 3, "number(s) divisible by six")
print(divide_seven, "number(s) divisible by seven")
print(divide_two // 4, "number(s) divisible by eight")
print(divide_three // 3, "number(s) divisible by nine")
