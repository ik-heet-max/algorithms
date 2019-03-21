sum = 0
NUM = -2
n = int(input("Enter power: "))
for i in range(0, n+1):
    sum += (NUM ** (-i))
print(sum)
