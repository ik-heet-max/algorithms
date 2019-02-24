import random

num = random.randint(0, 100)
for i in range(10):
    guess = int(input("Guess the number (from 0 to 100): "))
    if i < 9:
        if guess == num:
            print("Yippeeeee! You've hit it!")
            exit(0)
        elif guess < num:
            print("Wrong. Try something bigger than that.")
        else:
            print("Wrong. Try something smaller than that.")
    else:
        if guess == num:
            print("Yippeeeee! You've hit it!")
            exit(0)
        else:
            print("The number I've thought of is", num)
