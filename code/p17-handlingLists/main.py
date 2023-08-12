# numbers = [3, 5, 1, 20, 3, 2, 5, 20, 13, 4]
#
# print(numbers)
#
# numbers.append(5)
# print(numbers)
#
# numbers.pop()
# print(numbers)
#
# numbers[5] = 1000
# print(numbers)
#
# numbers.clear()
# print(numbers)

numbers = [4, 12, 4, 15, 23, 1, 0, -5, 12, 20, 7, 9]
smallNumbers = []
bigNumbers = []

# exercise
# read the numbers list and append numbers < 10 to the small numbers list
# and to the big numbers list if they are 10 or bigger


numberList = [4, 5, 2, 1, 19, 3, 2, 1, 4, 6, 4, 3, 2, 1, 5, 6, 4, 4, 6, 2]
shortList = []
# [4, 5, 2, 1, 19, 3, 6]

for number in numberList:
    if number not in shortList:
        shortList.append(number)

print(shortList)

# data scientist
# data engineer
    # code (usually in python)
    # know databases