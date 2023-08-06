print("please enter a value and I will sum:")
n = input("> ")
n = int(n)

total = 0
resultText = ""

for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        total += i

        if i > 3:
            resultText += " + "
        resultText += str(i)

resultText += " = "
resultText += str(total)

print(resultText)


