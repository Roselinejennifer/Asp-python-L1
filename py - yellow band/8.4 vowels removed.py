def remove_vowels(input_string):
    vowels = "aeiouAEIOU"  # Define a string containing all vowels

    # Use list comprehension to create a new string with characters that are not vowels
    new_string = ''.join([char for char in input_string if char not in vowels])

    return new_string


# Example usage:
input_string = "Hello, World!"
print("String with vowels removed:", remove_vowels(input_string))
