import sqlite3
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, "jwt_database.db")
conn = sqlite3.connect(db_path)

# Create a cursor
cursor = conn.cursor()

# Create the tokens table
cursor.execute("""CREATE TABLE tokens (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    jwt TEXT NOT NULL
)""")

# Commit the changes
conn.commit()

# Close the connection
conn.close()
