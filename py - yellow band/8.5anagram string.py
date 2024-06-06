def are_anagrams(str1, str2):
    # Convert both strings to lowercase for case-insensitive comparison
    str1 = str1.lower()
    str2 = str2.lower()

    # Remove spaces from both strings
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    # Check if the lengths of the strings are equal
    if len(str1) != len(str2):
        return False

    # Sort the characters in both strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # Check if the sorted strings are equal
    if sorted_str1 == sorted_str2:
        return True
    else:
        return False


# Example usage:
string1 = "listen"
string2 = "silent"
print("Are the strings anagrams?", are_anagrams(string1, string2))
