numbers = [4, 5, 6, 1, 2, 8, 6]

# printing a list
# shows a representation of all elements in the list
print(numbers)

# printing a specific position
# positions start at 0
print(numbers[2])

# lists and for loops go great together
# for n in numbers:
#     print(n)

# exercise
# print the sum of all the numbers in the list

total = 0
for n in numbers:
    total = total + n
    print("current number: " + str(n))
    print("current total: " + str(total))
    print("-----------")

print("Total: " + str(total))

# len means length, always gives you
# the correct size of a list
avg = total / len(numbers)

# round with a precision of 2 decimal points
avg = round(avg, 2)

print("Average: " + str(avg))
