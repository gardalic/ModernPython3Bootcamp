import sqlite3


conn = sqlite3.connect("sql\practice\my_friends.db")
c = conn.cursor()

query = "SELECT * FROM friends"
c.execute(query)

# Can do this, but need to loop because it returns a tuple at a time
# for result in c:
#     print(result)

# This is better, returns the tuples in a single list
res_list = c.fetchall()

for item in res_list:
    print(item)

conn.close()
