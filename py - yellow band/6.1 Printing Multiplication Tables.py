def print_multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Demonstrating the use of the function
print("Multiplication table for 5:")
print_multiplication_table(5)
print("\nMultiplication table for 7:")
print_multiplication_table(7)
print("\nMultiplication table for 9:")
print_multiplication_table(9)
