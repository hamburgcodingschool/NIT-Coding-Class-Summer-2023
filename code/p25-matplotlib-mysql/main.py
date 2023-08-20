import mysql.connector
import matplotlib.pyplot as plt

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="world"
)
# print("What's your language?")
motherTongue = "portuguese"

cursor = db.cursor()
sql = f"""
SELECT CountryCode, Name, Population * Percentage / 100 / 1000000 AS Speakers, Language
FROM countrylanguage
JOIN country ON country.code = countrylanguage.countrycode
WHERE Language LIKE '%{motherTongue}%'
HAVING Speakers > 0
"""

print(sql)
cursor.execute(sql)
result = cursor.fetchall()

countries = []
population = []

if len(result) > 0:
    for row in result:
        countries.append(row[0])
        population.append(row[2])


else:
    print("I'm sorry, there's no such info.")

print(countries)
print(population)

plt.ylabel("Population (in millions)")

counter = 0
for populationNumber in population:
    numberLabel = str(round(populationNumber, 2))
    plt.text(counter, populationNumber, numberLabel, ha='center')
    counter += 1

plt.bar(countries, population)
plt.show()
