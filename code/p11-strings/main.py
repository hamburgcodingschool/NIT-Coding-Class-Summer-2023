# name = "Helder"
#
# count = 0
# for char in name:
#     if char == "e" or char == "E":
#         count += 1
#
# print(count)

# exercise ask the user for a name:
# print the name in reverse...
name = "Helder"
reverseName = ""

for pos in range(0, len(name)):
    lastPos = len(name) - 1
    reversePos = lastPos - pos
    reverseName = reverseName + name[reversePos]
    print(reversePos)
    print(name[reversePos])

print(reverseName)

# another solution
reverseName2 = ""
for char in name:
    reverseName2 = char + reverseName2

print(reverseName2)

