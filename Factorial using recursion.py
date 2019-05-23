def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x-1)

x=int(input("Enter the no : "))
print("Factorial of {} is {}".format(x,fact(x)))