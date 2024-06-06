def sum_of_even_numbers(numbers):
    """Return the sum of all even numbers in the given list."""
    return sum(num for num in numbers if num % 2 == 0)

# Example usage:
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_even = sum_of_even_numbers(input_list)
print("Sum of even numbers:", sum_even)
