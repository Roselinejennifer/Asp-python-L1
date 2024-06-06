fruits = {
    'apple':50,
    'banana':25,
    'orange':75,
    'strawberry':100
}
apple_price = fruits['apple']
print("An apple costs :", apple_price)

# Now let's say we want to add a new fruit to the dictionary
fruits['mango'] = 125
print(fruits)

del fruits['apple']
print(fruits)