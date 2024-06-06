items={"PAPADAM":10,
       "CHIPS":10,
       "CHOCLATES":50,
       "CAKES":60}
money_inserted=int(input("Enter the amount of money you want to insert: "))
while money_inserted>0:
    for item,price in items.items():
        print(item+" " + str(price))
    choice=input("\nEnter the item you want to purchase(or 'exit' to exit):")
    choice=choice.upper()

    if choice== 'exit':
        break;

    if choice in items:
        if money_inserted < items[choice]:
            print("sorry you dont have enough money to purchase this item.")
        else:
            money_inserted=money_inserted-items[choice]
            print("you purchased "+choice +" for "+str(items[choice]) +" and you have "+str(money_inserted)+" remaining")
    else:
        print("sorry that item is not avialable")