import csv

dummyData = [
    ("Helder", 42, "Porto"),
    ("Martha", 20, "NY"),
    ("Bob", 31, "London"),
    ("Lydia", 50, "Paris")
]

# Creating / Opening a new file in "w" write mode
file = open("example1.csv", "w")

# Creating a variable that allows to write CSV  (COMMA SEPARATED VALUES) data into the open file
writer = csv.writer(file)

# write a row of data into the CSV
writer.writerow(["Name", "Age", "City"])
for dummy in dummyData:
    writer.writerow(dummy)

# at the end, nothing left to write to the file so close it
file.close()
