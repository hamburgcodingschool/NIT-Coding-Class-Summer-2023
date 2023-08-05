# EXERCISE 2

print("Hi I am doing \"fine\"...")
print("C:\\myFiles\\\\\\")
print("Hello\tWorld")
print("I am writing some text\nthis is in a new line")
print(" (3x3) ")

print(" ￼      _______          ")
print("       //  ||\\ \\       ")
print(" _____//___||_\\ \\___   ")
print(" )  _          _    \\   ")
print(" |_/ \\________/ \\___|  ")
print("___\\_/________\\_/______")

# EXERCISE 4
# print("Number please?")
# n = int(input("> "))
#
# total = 0
# result = ""
# for i in range(1, n + 1):
#     if i > 1:
#         result = result + " + "
#     result = result + str(i)
#
#     total = total + i
#
# print(result + " = " + str(total))

# RESULT LOOKS LIKE:
# 1 + 2 + 3 + 4 + 5 + 6 = 21


# EXERCISE 5
# todo: ask user for input later
n = 20

total = 0
for i in range(1, n + 1):
    if i % 3 == 0:
        print(i)
        total = total + i
    elif i % 5 == 0:
        print(i)
        total = total + i

print("-------")
print(total)
