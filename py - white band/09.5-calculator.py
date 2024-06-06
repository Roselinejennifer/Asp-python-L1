def calculator():
    print("Welcome to the Python Calculator!")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")

    operation = input("Enter operation (1/2/3/4/5): ")

    if operation in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == '1':
            result = num1 + num2
            print(f"The result of {num1} + {num2} is {result}")
        elif operation == '2':
            result = num1 - num2
            print(f"The result of {num1} - {num2} is {result}")
        elif operation == '3':
            result = num1 * num2
            print(f"The result of {num1} * {num2} is {result}")
        elif operation == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is {result}")
            else:
                print("Error! Division by zero.")
        elif operation == '5':
            result = num1 % num2
            print(f"The result of {num1} % {num2} is {result}")
    else:
        print("Invalid operation selected")


def get_grade():
    score = float(input("Enter the student's score (0-100): "))

    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    print(f"The student's grade is: {grade}")


# Main function to run the calculator and grade functions
def main():
    while True:
        print("\nMain Menu")
        print("1. Use Calculator")
        print("2. Get Student Grade")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            calculator()
        elif choice == '2':
            get_grade()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")


# Run the main function
if __name__ == "__main__":
    main()
