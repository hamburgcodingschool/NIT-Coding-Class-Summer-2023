# print(type("Helder"))
# print(type(100))
# print(type(5.5))
# print(type(True))
# print(type("100"))
# print(type([23, 23, 345, 3, 2]))
# print(type(["Helder", "Julie", "Someone else"]))

exchangeRateUSDtoEuro = 0.91

print("The current exchange rate from Euro to USD is " + str(exchangeRateUSDtoEuro))
print("Please enter an amount in dollars")
inputAmount = input("> $")

usdAmount = float(inputAmount)
euroAmount = usdAmount * exchangeRateUSDtoEuro

euroAmount = round(euroAmount, 2)

print("€" + str(euroAmount))
