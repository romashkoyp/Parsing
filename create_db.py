import sqlite3

# Connect to the database (this will create it if it doesn't exist)
conn = sqlite3.connect('words.db')
cursor = conn.cursor()

# Create a table named 'all_words' if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS all_words (
        id INTEGER PRIMARY KEY,
        word TEXT,
        type TEXT
    )
''')

conn.commit()
conn.close()

