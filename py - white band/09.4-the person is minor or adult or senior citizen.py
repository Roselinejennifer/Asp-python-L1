age =  int(input("enter your age:"))
if age < 0:
    print("invalid age, please enter a non-negative number.")
elif age < 18:
    print("you are a minor")
elif age < 65:
    print("you are an adult")
else:
    print("you are a senior citizen")