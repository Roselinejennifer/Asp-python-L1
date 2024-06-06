age = int(input("How old are you?: "))
bornInUS = input("Were you born in the US?: ")
residency = int(input("How many years of residency do you have?: "))

isEligible = True

if age < 35:
    isEligible = False
if bornInUS == "no":
    isEligible = False
if residency < 14:
    isEligible = False

if isEligible:
    print("You are eligible for president!")
else:
    print("You are not eligible for president.")