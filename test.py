#test
import sqlite3

curr = sqlite3.connect(r"C:\Users\yo-s-\Documents\GitHub\ai-chef\sqlite\database.db")
cursor = curr.cursor()

query = "SELECT * FROM users"
cursor.execute (query)

results = cursor.fetchall()

for i in results:
    print(i)

query2 = "SELECT * FROM pantry"
cursor.execute (query2)

results2 = cursor.fetchall()

for i in results2:
    print(i)

cursor.close()
curr.close()