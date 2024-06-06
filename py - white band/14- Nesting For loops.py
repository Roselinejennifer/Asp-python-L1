fruits = ["apples", "oranges", "mangoes"]

for fruit in fruits:

    string_size = 0

    for alphabet in fruit:

        string_size += 1

    print("name of fruit: %s is has length %s" % (fruit, string_size))