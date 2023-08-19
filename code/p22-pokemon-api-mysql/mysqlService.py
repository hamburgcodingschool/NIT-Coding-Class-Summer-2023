import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="pokemon_data"
)

def insertPokemon(newPokemon):

    cursor = db.cursor()
    sql = f"""
        INSERT INTO pokemon
        (id, name, height, weight, official_artwork)
        VALUES
        ({newPokemon["id"]}, "{newPokemon["name"]}", {newPokemon["height"]}, {newPokemon["weight"]}, "{newPokemon["image"]}")
        """

    cursor.execute(sql)
    # Queries need to be commited after execution
    db.commit()


def selectAllPokemon():
    cursor = db.cursor()
    sql = """
    SELECT *
    FROM pokemon
    ORDER BY name ASC
    LIMIT 5
    """

    cursor.execute(sql)
    result = cursor.fetchall()

    print(result)