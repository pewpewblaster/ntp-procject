# Utility to print the database, becouse this application is using
# SQLite3 precompiled C library and no cliend is present
import os
import sqlite3

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Create a connection to the database
db_path = os.path.join(current_dir, "jwt_database.db")
conn = sqlite3.connect(db_path)

cursor = conn.cursor()
cursor.execute("SELECT * FROM tokens")
rows = cursor.fetchall()
column_names = [description[0] for description in cursor.description]

print(column_names)
for row in rows:
    print(row)

conn.close()
