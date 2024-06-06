word = input("Enter word: ")
reversed_word = word[::-1]

if word == reversed_word:
	print("It is palindrome.")
else:
	print("It is not palindrome.")