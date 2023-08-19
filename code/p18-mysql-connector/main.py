import mysql.connector

# we create a connection to our mysql database
# and store it in a variable called `db`
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="world"
)

# we tell the database to create a cursor
# the cursor will be used to execute and fetch SQL queries
cursor = db.cursor()

# we add the sql to the cursor
# and execute the query
sql = """
SELECT *
FROM city
ORDER BY name ASC
LIMIT 5
"""

print(sql)
cursor.execute(sql)

# and now we will extract the data from the cursor
# this data is the result of the previous execute command
result = cursor.fetchall()

for city in result:
    print(city[2])

# multilineString = ("Hello "
#                    "Julie")
# print(multilineString)
#
# otherMultilineString = """
# Hello
# Helder"""
#
# print(otherMultilineString)

# CONCATENATION

name = "Bob"
greeting = "Hello " + name + " how are you doing?"
print(greeting)

# String FORMATTING
name = "Bob"
greeting = "Hello {} how are you doing?".format(name)
print(greeting)

# fString (available since Python 3.6)
name = "Bob"
greeting = f"Hello {name} how are you doing?"
print(greeting)


