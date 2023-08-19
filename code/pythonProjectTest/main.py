import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="world"
)

print(mydb)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM city")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)