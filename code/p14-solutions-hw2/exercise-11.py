numbers = [4, 7, 10, 12, 1, 8, 20, 16]
# Sum: 78
# Average: 9.75
# Highest: 20
# Lowest: 1

total = 0
highest = numbers[0]
lowest = numbers[0]
for n in numbers:
    total += n

    if n > highest:
        highest = n

    if n < lowest:
        lowest = n

avg = total / len(numbers)

print("Sum: " + str(total))
print("Average: " + str(avg))
print("Highest: " + str(highest))
print("Lowest: " + str(lowest))
