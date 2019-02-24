even = 0
odd = 0
number = input("Enter number: ")
for i in number:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1
print(even, " even digits")
print(odd, " odd digits")