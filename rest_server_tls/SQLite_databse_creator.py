import ctypes
sqlite3 = ctypes.CDLL('SQLite/sqlite3.dll')

import sqlite3
db_connection = sqlite3.connect('jwt_database.db')  # Replace with your desired database name
db_cursor = db_connection.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    jwt_token TEXT
)
'''

db_cursor.execute(create_table_query)
db_connection.commit()

db_connection.close()