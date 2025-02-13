import sqlite3

# Connect to the database
conn = sqlite3.connect("bincom_test.sqlite")
cursor = conn.cursor()

# Insert sample data into the table
cursor.execute("INSERT INTO sample_table (name, age) VALUES ('Alice', 25)")
cursor.execute("INSERT INTO sample_table (name, age) VALUES ('Bob', 30)")
cursor.execute("INSERT INTO sample_table (name, age) VALUES ('Charlie', 22)")

# Commit changes and close connection
conn.commit()
conn.close()

print("Sample data inserted successfully!")
