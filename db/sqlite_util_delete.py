import sqlite3
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

# Create a connection to the database
db_path = os.path.join(current_dir, "jwt_database.db")
# Connect to the SQLite database
db_connection = sqlite3.connect(db_path)  # Replace with your database name
db_cursor = db_connection.cursor()

# Delete all data from the 'tokens' table
db_cursor.execute('DELETE FROM tokens;')

# Commit the changes and close the connection
db_connection.commit()
db_connection.close()

print("All data from the 'tokens' table has been deleted.")
