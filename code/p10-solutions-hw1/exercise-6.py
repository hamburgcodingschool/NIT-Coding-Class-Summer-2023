print("please enter a value:")
n = input("> ")
n = int(n)

print("Would you like to calculate the sum(S) or the product(P)")
choice = input("P/S >")

while choice != "P" and choice != "S":
    print("Invalid choice. Try again:")
    choice = input("P/S >")

if choice == "S":
    total = 0
    resultText = ""

    for i in range(1, n + 1):
        total += i

        if i > 1:
            resultText += " + "
        resultText += str(i)

    resultText += " = "
    resultText += str(total)
    print(resultText)

elif choice == "P":
    total = 1
    resultText = ""

    for i in range(1, n + 1):
        total *= i

        if i > 1:
            resultText += " x "
        resultText += str(i)

    resultText += " = "
    resultText += str(total)
    print(resultText)
