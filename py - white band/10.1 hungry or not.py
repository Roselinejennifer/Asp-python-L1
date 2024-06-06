hungry = input("Are you hungry? (Yes/No)")

if hungry.lower() == "yes":

  hungry = True
else:

  hungry = False


if hungry:
  print("You should eat something!")
else:
  print("You are not hungry. You can wait to eat.")