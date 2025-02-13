import sqlite3

def create_tables():
    conn = sqlite3.connect("bincom_test.sqlite")
    cursor = conn.cursor()

    # Example table: Modify based on your actual data
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sample_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Database tables created successfully!")
