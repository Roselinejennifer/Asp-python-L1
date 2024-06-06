correct_password = "python123"
password = input("enter the password:")
while password != correct_password:
    print("incorrect password. try again.")
    password = input("enter the password:")
print("access granted!")