import csv
import random

file = open("names.csv")

reader = csv.reader(file)

# I don't want the header
# so I call next to jump the first line
next(reader)

names = []
for row in reader:
    names.append(row[1])

winner = random.sample(names, 1)
print(winner)
