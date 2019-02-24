n = int(input("Enter number: "))
sum = 0
for i in range(n + 1):
    sum += i
print(sum)
if sum == n * (n + 1) / 2:
    print("It works!")
else:
    print("Doesn't work :(")