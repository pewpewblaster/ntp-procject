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

# funkcija za kreiranje novog usera na formi create_user_form.py
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

# funkcija za importanje itema u dadtabazu skladiste.proizvodi
def import_product(warehouse_id,
                    product_name,
                    product_price,
                    product_quantity,
                    product_category):

    if warehouse_id and product_name and product_price and product_quantity and product_category:
        database_skladiste = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=db/skladiste.accdb;')
        query = database_skladiste.cursor()

        insert_query = 'INSERT INTO proizvodi (skladiste_id, naziv, cijena, kolicina, kategorija) ' \
                        'VALUES (?, ?, ?, ?, ?)'
        query.execute(insert_query, warehouse_id, product_name, product_price, product_quantity, product_category)
        database_skladiste.commit()

        query.close()
        database_skladiste.close()

        print("Product imported successfully.")
        
def import_warehouse(
                    warehouse_name,
                    warehouse_address,
                    warehouse_city,
                    warehouse_country):

    if warehouse_name and warehouse_address and warehouse_city and warehouse_country:
        database_skladiste = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=db/skladiste.accdb;')
        query = database_skladiste.cursor()

        insert_query = 'INSERT INTO skladista (naziv_skladista, adresa, grad, drzava) ' \
                        'VALUES (?, ?, ?, ?)'
        query.execute(insert_query, warehouse_name, warehouse_address, warehouse_city, warehouse_country)
        database_skladiste.commit()

        query.close()
        database_skladiste.close()

        print("Warehouse imported successfully.")


def get_table(warehouse_id):
    database_skladiste = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=db/skladiste.accdb;')
    query = database_skladiste.cursor()
    
    query_insert = '''
        SELECT *
        FROM skladista
        INNER JOIN proizvodi ON skladista.skladiste_id = proizvodi.skladiste_id
        WHERE skladista.skladiste_id = ?
    '''
    
    query.execute(query_insert, (warehouse_id,))
    header = [description[0] for description in query.description]
    table = query.fetchall()
    print("Table loaded successfully.")
    
    query.close()
    database_skladiste.close()
    
    return table, header

