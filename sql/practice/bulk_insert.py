import sqlite3

conn = sqlite3.connect("sql\practice\my_friends.db")
c = conn.cursor()

people = [
    ("Roald", "Amundsen", 5),
    ("Rosa", "Parks", 8),
    ("Henry", "Hudson", 7),
    ("Neil", "Armstrong", 7),
    ("Daniel", "Boone", 3),
]
query = "INSERT INTO friends VALUES (?, ?, ?)"

c.executemany(query, people)
conn.commit()
conn.close()
