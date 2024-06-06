guest_list = ["jac", "jeni", "John"]

name = input("Enter your name: ")

if name in guest_list:
	print("Hello, " + name + "!")
else:
	print("Sorry, your name is not on my guest list.")
