import sqlite3

conn = sqlite3.connect("my_friends.db")
c = conn.cursor()
# sql_statement = "CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER)"
# sql_statement = "INSERT INTO friends VALUES ('Merriwether', 'Lewis', 7)"

# form_data = "Mary-Todd"
# query = "INSERT INTO friends (first_name) VALUES (?)"

data = ("Steve", "Irvin", 9)
query = "INSERT INTO friends VALUES (?, ?, ?)"

c.execute(query, data)
conn.commit()
conn.close()
