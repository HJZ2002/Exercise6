TheSum = 0.0
TheAverage = 0.0
TheDivided = 0.0

name = int(input("Enter a number or press enter to quit"))

while name != "":
    TheSum += float(name)
    TheDivided += 1
    name = input("Enter a number or press enter to quit")

TheAverage = TheSum/TheDivided

print("The sum is ", TheSum)
print("The Average is", TheAverage)