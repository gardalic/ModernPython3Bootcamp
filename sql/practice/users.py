import sqlite3

conn = sqlite3.connect("sql/practice/users.db")
c = conn.cursor()
create_table = "CREATE TABLE users (username TEXT, password TEXT)"

# c.execute(create_table)

try:
    c.execute(create_table)
except sqlite3.OperationalError:
    print("Table already exists, skipping creation...")

username = input("Please enter your username: ")
p = input("Please enter your password: ")
# query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{p}'"
query = "SELECT * FROM users WHERE username = ? AND password = ?"

c.execute(query, (username, p))

result = c.fetchone()
if result:
    print("Welcome back!")
else:
    print("FAILED LOGIN")

conn.close()
