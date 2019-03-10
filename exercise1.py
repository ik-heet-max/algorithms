while True:
    n = float(input("Enter first term: "))
    m = float(input("Enter second term: "))
    op = input("What operation to perform (enter sign)? ")
    if op == '0':
        exit(0)
    elif op == '+':
        print("The sum is ", n + m)
    elif op == '-':
        print("The remainder is ", n - m)
    elif op == '*':
        print("The product is ", n * m)
    elif op == '/':
        if m == 0:
            print("Division by zero! We're screwed!")
        else:
            print("The quotient is ", n / m)
    else:
        print("Wrong operation sign. Try again.")