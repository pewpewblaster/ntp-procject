import pyodbc

# connector for user credenitals databse

def user_database():
    connection_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=db/users.accdb;'
    database_users = pyodbc.connect(connection_string)
    
    query = database_users.cursor()
    query.execute("SELECT username FROM credentials")
    users = query.fetchall()
    
    # query.fetchall return list that looks like this [('admin', ), ('Username', ), ('matija', ), ('jurica', ), ('jure', ), ('', ), ('matija2', )]
    # save tuples values with index 0 to a new list called users_list
    users_list = [username[0] for username in users]
    
    query.close()
    database_users.close()
    
    # returns list with all usernames from databse users table credentials
    return users_list

def delete_product_by_id(product_id):
    database_skladiste = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=db/skladiste.accdb;')
    query = database_skladiste.cursor()
    
    select_query = '''
        SELECT *
        FROM proizvodi
        WHERE proizvod_id = ?
    '''
    query.execute(select_query, (product_id,))
    
    result = query.fetchone() # (1, 'Skladiste 1', '123 Main St', 'New York', 'USA')
    
    # ako ne postoji skladiste sa trazenim skladiste_id
    if not result:
        query.close()
        database_skladiste.close()
        print(f"Ne postji produkt sa id: {product_id}!")
        return False

    
    delete_query = '''
            DELETE FROM proizvodi
            WHERE proizvod_id = ?
        '''

    query.execute(delete_query, (product_id,))
    query.commit()

    query.close()
    database_skladiste.close()
    
    return True
def delete_warehouse_by_id(warehouse_id):
    database_skladiste = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=db/skladiste.accdb;')
    query = database_skladiste.cursor()
    
    select_query = '''
        SELECT *
        FROM skladista
        WHERE skladiste_id = ?
    '''
    query.execute(select_query, (warehouse_id,))
    
    result = query.fetchone() # (1, 'Skladiste 1', '123 Main St', 'New York', 'USA')
    
    # ako ne postoji skladiste sa trazenim skladiste_id
    if not result:
        query.close()
        database_skladiste.close()
        print(f"Ne postji skladsite sa id: {warehouse_id}!")
        return False

    
    delete_query = '''
            DELETE FROM skladista
            WHERE skladiste_id = ?
        '''

    query.execute(delete_query, (warehouse_id,))
    query.commit()

    query.close()
    database_skladiste.close()
    
    return True

def delete_user_from_database(username_for_deletion):
    connection_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=db/users.accdb;'
    database_users = pyodbc.connect(connection_string)
    
    query = database_users.cursor()
    query.execute("SELECT username FROM credentials")
    users = query.fetchall()
    
    # query.fetchall return list that looks like this [('admin', ), ('Username', ), ('matija', ), ('jurica', ), ('jure', ), ('', ), ('matija2', )]
    # save tuples values with index 0 to a new list called users_list
    users_list = [username[0] for username in users]
    
    if username_for_deletion not in users_list:
        print("Can not delete username that is not inside the database")
        query.close()
        database_users.close()
        return False
    else:
        query.execute("DELETE FROM credentials WHERE username = ?", username_for_deletion)
        database_users.commit()
        query.close()
        database_users.close()
        print("Usere deleted from database")
        return True
    
def change_password(username_for_password_changing, new_password):
    connection_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=db/users.accdb;'
    database_users = pyodbc.connect(connection_string)
    
    query = database_users.cursor()
    query.execute("SELECT username FROM credentials")
    users = query.fetchall()
    
    # query.fetchall return list that looks like this [('admin', ), ('Username', ), ('matija', ), ('jurica', ), ('jure', ), ('', ), ('matija2', )]
    # save tuples values with index 0 to a new list called users_list
    users_list = [username[0] for username in users]
    
    if username_for_password_changing not in users_list:
        print("Cannot change password for a username that is not inside the database")
        query.close()
        database_users.close()
        return False
    else:
        query.execute("UPDATE credentials SET password = ? WHERE username = ?", (new_password, username_for_password_changing))
        database_users.commit()
        query.close()
        database_users.close()
        print("Password changed successfully")
        return True


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
        
def import_warehouse(warehouse_name,
                     warehouse_address,
                     warehouse_city,
                     warehouse_county):
    
    if warehouse_name and warehouse_address and warehouse_city and warehouse_county:
        database_skladiste = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=db/skladiste.accdb;')
        query = database_skladiste.cursor()
        
        insert_query = 'INSERT INTO skladista (naziv_skladista, adresa, grad, drzava)' \
                        'VALUES (?, ?, ?, ?)'
        query.execute(insert_query, warehouse_name, warehouse_address, warehouse_city, warehouse_county)
        database_skladiste.commit()
        
        query.close()
        database_skladiste.close()
        
        print("Warehouse imported successfully.")

# funkcija za update atributa skadista po skladite_id, ako se field ostavi prazan,
# zapise se stara vrijenost (tj, ostane nepromijenjena)
def update_warehouse(warehouse_id,
                     warehouse_name,
                     warehouse_address,
                     warehouse_city,
                     warehouse_country
                     ):
    
    database_skladiste = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=db/skladiste.accdb;')
    query = database_skladiste.cursor()
    
    select_query = '''
        SELECT *
        FROM skladista
        WHERE skladiste_id = ?
    '''
    query.execute(select_query, (warehouse_id,))
    
    result = query.fetchone() # (1, 'Skladiste 1', '123 Main St', 'New York', 'USA')
    
    # ako ne postoji skladiste sa trazenim 
    if not result:
        query.close()
        database_skladiste.close()
        print(f"Ne postji skladsite sa id: {warehouse_id}!")
        return False
    
    old_value_name = result[1]
    old_value_address = result[2]
    old_value_city = result[3]
    old_value_country = result[4]
    
    new_value_name = old_value_name if not warehouse_name else warehouse_name
    new_value_address = old_value_address if not warehouse_address else warehouse_address
    new_value_city = old_value_city if not warehouse_city else warehouse_city
    new_value_country = old_value_country if not warehouse_country else warehouse_country
    
    update_query = '''
        UPDATE skladista
        SET naziv_skladista = ?,
            adresa = ?,
            grad = ?,
            drzava = ?
        WHERE skladiste_id = ?
    '''

    query.execute(update_query, (new_value_name, 
                                 new_value_address, 
                                 new_value_city, 
                                 new_value_country, 
                                 warehouse_id))
    query.commit()

    query.close()
    database_skladiste.close()
    
    return True

def update_product(product_id,
                   warehouse_id,
                   product_name,
                   product_price,
                   product_quantity,
                   product_category):
    
    database_skladiste = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=db/skladiste.accdb;')
    query = database_skladiste.cursor()
    
    select_query = '''
        SELECT *
        FROM proizvodi
        WHERE proizvod_id = ?
    '''
    query.execute(select_query, (product_id,))
    
    result = query.fetchone()
    
    if not result:
        query.close()
        database_skladiste.close()
        print(f"Ne postji proizvod sa id: {product_id}!")
        return False
    
 
    old_value_product_name = result[1]
    old_value_product_price = result[2]
    old_value_product_quantity = result[3]
    old_value_warehousu_id = result[4]
    old_value_product_category = result[5]

    print(old_value_warehousu_id)
    print(old_value_product_name)
    print(old_value_product_price)
    print(old_value_product_quantity)
    print(old_value_product_category)
    
    new_value_warehouseid = old_value_warehousu_id if not warehouse_id else warehouse_id
    new_value_product_name = old_value_product_name if not product_name else product_name
    new_value_product_price = old_value_product_price if not product_price else product_price
    new_value_product_quantity = old_value_product_quantity if not product_quantity else product_quantity
    new_value_product_category = old_value_product_category if not product_category else product_category

    print(f"new values:\n{new_value_warehouseid}\n{new_value_product_name}\n{new_value_product_price}\n{new_value_product_quantity}\n{new_value_product_category}\n")
    
    update_query = '''
        UPDATE proizvodi
        SET naziv = ?,
            cijena = ?,
            kolicina = ?,
            skladiste_id = ?,
            kategorija = ?
        WHERE proizvod_id = ?
    '''   

    query.execute(update_query, (new_value_product_name, 
                                 new_value_product_price, 
                                 new_value_product_quantity, 
                                 new_value_warehouseid, 
                                 new_value_product_category,
                                 product_id))
    query.commit()

    query.close()
    database_skladiste.close()
    
    return True
    
    

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
    
    
    query_insert = "SELECT skladiste_id FROM skladista"
    query.execute(query_insert)
    list_of_skladiste_id = [row.skladiste_id for row in query.fetchall()]

    query.close()
    database_skladiste.close()
    print(table)
    return table, header, list_of_skladiste_id

def get_table_by_filter(filter_product_by_name):
    database_skladiste = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=db/skladiste.accdb;')
    query = database_skladiste.cursor()
    
    query_insert = '''
        SELECT *
        FROM skladista
        INNER JOIN proizvodi ON skladista.skladiste_id = proizvodi.skladiste_id
        WHERE proizvodi.naziv = ?
    '''
    query.execute(query_insert, (filter_product_by_name,))
    table = query.fetchall()

        
    header = [description[0] for description in query.description]

    # ako query prodje u 'has_result' se zapise True, suprutno False
    has_result = bool(table)

    query.close()
    database_skladiste.close()
    print(table)
    return table, header, has_result

def show_table(table_id):
    database_skladiste = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=db/skladiste.accdb;')
    query = database_skladiste.cursor()
    
    if table_id == "warehouse":
        query.execute("SELECT * FROM skladista")
        table = query.fetchall()
        header = [description[0] for description in query.description]
        table_array = [list(t) for t in table]
    
    if table_id == "product":
        query.execute("SELECT * FROM proizvodi")
        table = query.fetchall()
        header = [description[0] for description in query.description]
        table_array = [list(t) for t in table]

    query.close()
    database_skladiste.close()
    
    return table_array, header

''' testni dio za funkcije'''

