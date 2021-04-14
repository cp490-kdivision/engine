import sqlite3

def get_id(coal_engine_db, game_ID):
    query = "SELECT game_ID FROM Game WHERE id=?;"
    connection = sqlite3.connect(coal_engine_db)
    cursor = connection.cursor()
    cursor.execute(query,[game_ID])
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results
    print("Your Game ID is: ", game_ID('coal_engine_db'))

def get_games(coal_engine_db, game_Name):
    query = "SELECT game_Name FROM Game"
    connection = sqlite3.connect(coal_engine_db)
    cursor = connection.cursor()
    cursor.execute(query,[game_Name])
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results
    print("Welcome To : ", game_Name('coal_engine_db'))

def get_description(coal_engine_db, game_Description):
    query = "SELECT game_Description FROM Game"
    connection = sqlite3.connect(coal_engine_db)
    cursor = connection.cursor()
    cursor.execute(query,[game_Description])
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results
    print("General Description : ", game_Description('coal_engine_db'))