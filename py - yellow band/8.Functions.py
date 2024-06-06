def addition(num1, num2):
    print("The answer is: " + str(num1 + num2))

def subtraction(num1, num2):
    print("The answer is: " + str(num1 - num2))

def multiplication(num1, num2):
    print("The answer is: " + str(num1 * num2))

def division(num1, num2):
    print("The answer is: " + str(num1 / num2))

while True:
    num1 = int(input("Enter a number: "))
    op = input("Enter an operation (+,-,*,/): ")
    num2 = int(input("Enter another number: "))

    if op == "+":
        addition(num1, num2)
    elif op == "-":
        subtraction(num1, num2)
    elif op == "*":
        multiplication(num1, num2)
    elif op == "/":
        division(num1, num2)
    else:
        print("Invalid input!")
    run = input("Would you like to continue? (y/n): ")
    if run == "n":
        break