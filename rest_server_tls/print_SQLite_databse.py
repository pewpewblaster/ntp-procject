import sqlite3
import ctypes

# Load the SQLite DLL
# sqlite3_dll = ctypes.CDLL('SQLite/sqlite3.dll')

# Establish a connection to the SQLite database
connection = sqlite3.connect("jwt_database.db")  # Replace with your database file name

# Create a cursor object
cursor = connection.cursor()

# Execute the SQL query to retrieve data from the "users" table
query = "SELECT * FROM users"
cursor.execute(query)

# Fetch all rows from the result
users = cursor.fetchall()

# Print the retrieved data
for user in users:
    print(user)

# Close the cursor and the connection
cursor.close()
connection.close()
