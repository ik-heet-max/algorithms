dig = input("Enter digits: ")
to_count = int(input("Enter digit you want to count: "))
count = 0
for i in dig:
    if int(i) == to_count:
        count += 1
print("The entered sequence contains", count, "digits")