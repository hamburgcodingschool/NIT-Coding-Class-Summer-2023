names = ["Josie", "Cathrin", "Bob Bobby-o", "Maxwell Pendleton", "Hannah", "Alex"]


longestName = names[0]
for name in names:
    numberOfChars = len(name)
    print(name + ": " + str(numberOfChars))

    if numberOfChars > len(longestName):
        longestName = name

print(longestName)
