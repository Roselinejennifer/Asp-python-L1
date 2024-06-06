num = int(input("Enter a number: "))

# using the modulus operator to check if there is a remainder
is_even = (num % 2) == 0

if is_even:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")