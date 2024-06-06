def calculator():
    # Displaying the options for the user
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Taking input from the user
    operation = input("Enter choice (1/2/3/4): ")

    if operation in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operation == '1':
                print(f"The result is: {num1 + num2}")
            elif operation == '2':
                print(f"The result is: {num1 - num2}")
            elif operation == '3':
                print(f"The result is: {num1 * num2}")
            elif operation == '4':
                if num2 != 0:
                    print(f"The result is: {num1 / num2}")
                else:
                    print("Error! Division by zero.")
        except ValueError:
            print("Invalid input! Please enter numerical values.")
    else:
        print("Invalid operation! Please choose a valid option.")

def main():
    while True:
        calculator()
        # Asking the user if they want to continue or quit
        continue_choice = input("Do you want to perform another calculation? (yes/no): ").lower()
        if continue_choice != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
