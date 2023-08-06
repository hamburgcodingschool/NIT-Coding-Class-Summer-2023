print("please enter a value and I will sum:")
n = input("> ")
n = int(n)

total = 0
resultText = ""

for i in range(1, n + 1):
    # the increment operator does exactly the same as this:
    # total = total + i
    total += i

    if i > 1:
        resultText += " + "
    resultText += str(i)

resultText += " = "
resultText += str(total)

print(resultText)

# someText = ""
#
# someText += "1"
#
# someText += " + "
# someText += "2"
#
# someText += " + "
# someText += "3"
#
# someText += " + "
# someText += "4"
#
# someText += " = "
# someText += "10"
#
# print(someText)