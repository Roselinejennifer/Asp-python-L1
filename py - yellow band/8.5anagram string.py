def are_anagrams(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    if len(str1) != len(str2):
        return False
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    if sorted_str1 == sorted_str2:
        return True
    else:
        return False
string1 = "listen"
string2 = "silent"
print("Are the strings anagrams?", are_anagrams(string1, string2))
