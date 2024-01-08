import sqlite3
import csv

conn = sqlite3.connect(r'C:\Users\romas\Documents\Code\Parsing\words.db')
cursor = conn.cursor()

# Assuming you have a table
with open(r'C:\Users\romas\Documents\Code\Parsing\Data\finnish_all_words.csv', 'r', newline='', encoding='utf-8-sig') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip the header row
    for row in csvreader:
        cursor.execute("INSERT INTO all_words (word, type) VALUES (?, ?)", (row[0], row[1]))

conn.commit()
conn.close()
