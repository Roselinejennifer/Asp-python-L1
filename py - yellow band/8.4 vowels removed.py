def remove_vowels(input_string):
    vowels = "aeiouAEIOU"  
    new_string = ''.join([char for char in input_string if char not in vowels])

    return new_string

input_string = "Hello, World!"
print("String with vowels removed:", remove_vowels(input_string))
