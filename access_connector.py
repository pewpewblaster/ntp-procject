import pyodbc

# connector for user credenitals databse

def user_database():
    connection_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=db/users.accdb;'
    database_users = pyodbc.connect(connection_string)
    
    query = database_users.cursor()
    query.execute("SELECT username, password FROM credentials")
    users = query.fetchall()
    
    query.close()
    database_users.close()
    
    # returns list with tuple (credentials inside of tuple)
    return users

# function for checking if username and password match at login
def check_credentials(username, password):
    connection_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=db/users.accdb;'
    database_users = pyodbc.connect(connection_string)
    
    query = database_users.cursor()
    query.execute("SELECT username, password FROM credentials WHERE username=? AND password=?", username, password)
    users = query.fetchone()
    
    query.close()
    database_users.close()
    
    if users is not None:
        print("Credentials found in the database.")
        return True
    else:
        print("Credentials not found in the database.")
        return False

def create_new_user(username, password):
    connection_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=db/users.accdb;'
    database_users = pyodbc.connect(connection_string)

    query = database_users.cursor()
    query.execute("SELECT username FROM credentials WHERE username=?", username)
    user = query.fetchone()

    
    if user is not None:
        print("Username already exists in the database.")
        query.close()
        database_users.close()
        return False
    else:
        query.execute("INSERT INTO credentials (username, password) VALUES (?, ?)", username, password)
        database_users.commit()
        query.close()
        database_users.close()
        print("Username and password saved to the database.")
        return True



 
    