import sqlite3

conn = sqlite3.connect("bincom_test.sqlite")  # Ensure this matches your database file name
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in database:", tables)

conn.close()
