total = 0
user_input = input("enter a number(type'stop'to end):")
while user_input.lower() != "stop":
    total += int(user_input)
    user_input = input("enter a number(type'stop' to end):")
print("sum of numbers:",total)