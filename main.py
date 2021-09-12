import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def factorial(x):
    return 1 if (x == 1 or x == 0) else x * factorial(x - 1);


print("Select operation -")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Factorial")
print("6.Sin")
print("7.Cos")
print("8.Tan")
print("9.Square root")
print("10.Power of a number")
print("11.Logarithm Value")
print("12.Natural logarithm")

while True:
    choice = input("Enter choice(1/2/3...): ")

    if choice in ('1', '2', '3', '4', '10'):
        val1 = float(input("Enter first number: "))
        val2 = float(input("Enter second number: "))

        if choice == '1':
            print(val1, "+", val2, "=", add(val1, val2))

        elif choice == '2':
            print(val1, "-", val2, "=", subtract(val1, val2))

        elif choice == '3':
            print(val1, "*", val2, "=", multiply(val1, val2))

        elif choice == '4':
            print(val1, "/", val2, "=", divide(val1, val2))

        elif choice == '10':
            print(val1, "^", val2, "=", val1**val2)

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    elif choice in ('5', '6', '7', '8', '9', '12'):
        val1 = float(input("Enter number: "))

        if choice == '5':
            print('Factorial of',val1,"is", factorial(val1))

        elif choice == '6':
            print('Sin value of',val1,'is', math.sin(val1))

        elif choice == '7':
            print('Cos value of',val1,'is', math.cos(val1))

        elif choice == '8':
            print('Tan value of',val1,'is', math.tan(val1))

        elif choice == '9':
            print('Square root of',val1,'is', math.sqrt(val1))

        elif choice == '12':
            print('Natural logarithm of',val1,'is', math.log(val1))


        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    elif choice in ('11'):
        val1 = float(input("Enter Base: "))
        val2 = float(input("Enter number: "))

        print("Logarithm base",val1,"of",val2,"is", math.log(val2,val1))

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")