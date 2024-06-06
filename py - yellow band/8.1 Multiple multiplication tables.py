def print_multiplication_table(num):
    print("Printing " + str(num) + " tables:")
    for i in range(1, 13):
        value = num * i
        print(str(num) + " x " + str(i) + " = " + str(value))

    print()  # Empty Line


# You can print the table for any number using just 1 line, without repetition.
print_multiplication_table(8)
print_multiplication_table(15)
print_multiplication_table(21)