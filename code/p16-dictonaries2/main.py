# students = ["Joe", "Martha", "Bob", "Ellie", "Claude"]
# grades = [3, 5, 4, 3, 5]

students = [
    {
        "name": "Joe",
        "grade": 3
    },
    {
        "name": "Martha the Third",
        "grade": 2
    },
    {
        "name": "Bob Bob Bob",
        "grade": 4
    },
    {
        "name": "Ellie",
        "grade": 3
    },
    {
        "name": "Claude",
        "grade": 5
    }
]

# 1 - I wanna know the name of the youngest
# 2 - I wanna know the name and age of the oldest
# 3 - I wanna know the age of the person with the longest name


# Exercise 1 solution
lowestGradedStudent = students[0]
for student in students:
    if student["grade"] < lowestGradedStudent["grade"]:
        lowestGradedStudent = student

print(lowestGradedStudent["name"])

# Exercise 2 solution
highestGradedStudent = students[0]
for student in students:
    if student["grade"] > highestGradedStudent["grade"]:
        highestGradedStudent = student

print(highestGradedStudent["name"])
print(highestGradedStudent["grade"])

# Exercise 3 solution
longestNamedStudent = students[0]
for student in students:
    if len(student["name"]) > len(longestNamedStudent["name"]):
        longestNamedStudent = student

print(longestNamedStudent["name"])
print(longestNamedStudent["grade"])

