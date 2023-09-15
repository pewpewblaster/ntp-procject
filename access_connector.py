import pyodbc
from salt_pepper.password_hesher import verify_password

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

# function for deleting product by id
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
    
    result = query.fetchone()  # (1, 'Skladiste 1', '123 Main St', 'New York', 'USA')
    
    # If the warehouse with the given ID doesn't exist
    if not result:
        query.close()
        database_skladiste.close()
        print(f"Ne postoji skladiste sa id: {warehouse_id}!")
        return False
    
    # Retrieve the related proizvod_id before deleting the warehouse
    proizvod_id_to_delete = result[0]  # Assuming the first column is proizvod_id

    delete_query_proizvod = '''
        DELETE FROM proizvodi
        WHERE skladiste_id = ?
    '''
    delete_query_skladiste = '''
        DELETE FROM skladista
        WHERE skladiste_id = ?
    '''

    try:
        query.execute(delete_query_proizvod, (warehouse_id,))
        query.execute(delete_query_skladiste, (warehouse_id,))
        query.commit()
        print(f"Skladiste sa id {warehouse_id} i pripadajući proizvodi su uspješno obrisani.")
        return True
    except Exception as e:
        query.rollback()
        print(f"Greška prilikom brisanja: {e}")
        return False
    finally:
        query.close()
        database_skladiste.close()


# function for deleting user by id
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
def check_credentials(username, input_password):
    
    
    connection_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=db/users.accdb;'
    database_users = pyodbc.connect(connection_string)
    
    query = database_users.cursor()
    # query.execute("SELECT username, password FROM credentials WHERE username=? AND password=?", username, password)
    # users = query.fetchone()

    query.execute("SELECT password FROM credentials WHERE username=? ", username)
    query_password = query.fetchall()
    query.close()
    database_users.close()
    
    if not query_password:
        return False
    
    password_to_verify = query_password[0][0]

    if verify_password(password_to_verify, input_password) == True:
        print("Credentials found in the database. Hashed password decoded.")
        return True
    else:
        print("Credentials not found in the database.")
        return False
    
    # if users is not None:
    #     print("Credentials found in the database.")
    #     return True
    # else:
    #     print("Credentials not found in the database.")
    #     return False

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

# function for 
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
    
    # last element is either type None or Binary string
    # for better performance we change it to True or False
    # to show if the element has imaage or not
    for table_element in table:
        if table_element[-1] != None:
            table_element[-1] = "True"
        else:
            table_element[-1] = "False"

    query.close()
    database_skladiste.close()
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
        
        # In the last element of the table_array list every character of the binary file was showm in the table column
        # That coused slow downs in the program. Now that cell shows if product has an image or not with values "True" of "False"
        for table_element in table_array:
            if table_element[-1] != None:
                table_element[-1] = "True"
            else:
                table_element[-1] = "False"

    query.close()
    database_skladiste.close()


    return table_array, header

def import_image(product_id, image_binary):
    database_skladiste = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=db/skladiste.accdb;')
    query = database_skladiste.cursor()

    update_query = '''
        UPDATE proizvodi
        SET privitak = ?
        WHERE proizvod_id = ?
    '''
    query.execute(update_query, (image_binary, product_id))
    query.commit()
    
    query.close()
    database_skladiste.close()
    
def get_image(product_id):
    database_skladiste = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=db/skladiste.accdb;')
    query = database_skladiste.cursor()

    select_quert = '''
        SELECT privitak
        FROM proizvodi
        WHERE proizvod_id = ?
    '''

    query.execute(select_quert, (product_id))
    image_binary = query.fetchone()
 
    # if function fails to get the image, it returns valeu (None, )
    if image_binary is None:
        return None

    return image_binary[0]

# function that collects data for RTF report on product
def get_product_data():

    database_skladiste = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=db/skladiste.accdb;')

    query = database_skladiste.cursor()
    query.execute('SELECT naziv, cijena, kolicina, skladiste_id, kategorija FROM proizvodi')

    product_data_dict = {}
    for row in query:
        naziv, cijena, kolicina, skladiste_id, kategorija = row
        product_data_dict[naziv] = {
            'cijena': cijena,
            'kolicina': kolicina,
            'skladiste_id': skladiste_id,
            'kategorija': kategorija,
        }

    query.close()
    database_skladiste.close()
    
    return product_data_dict

def get_master_detail_data():
    # Povezivanje s bazom
    database_skladiste = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=db/skladiste.accdb;')
    query = database_skladiste.cursor()
    query.execute('''
        SELECT s.skladiste_id, p.proizvod_id, p.naziv, p.cijena, p.kolicina, p.kategorija,
               IIF(p.privitak IS NOT NULL, True, False) AS privitak
        FROM [proizvodi] AS p
        INNER JOIN [skladista] AS s ON p.skladiste_id = s.skladiste_id;
    ''')

    # Dohvaćanje rezultata i izgradnja dictionary strukture
    master_detail = {}
    for row in query.fetchall():
        skladiste_id, proizvod_id, naziv, cijena, kolicina, kategorija, privitak = row
        if skladiste_id not in master_detail:
            master_detail[skladiste_id] = []
        
        proizvod = {
            'skladiste_id': skladiste_id,
            'proizvod_id': proizvod_id,
            'naziv': naziv,
            'cijena': cijena,
            'kolicina': kolicina,
            'kategorija': kategorija,
            'privitak': privitak
        }
        master_detail[skladiste_id].append(proizvod)

    # Zatvaranje veze s bazom
    query.close()
    database_skladiste.close()
    
    return master_detail

def get_image_for_pdf():
    
    database_skladiste = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=db/skladiste.accdb;')
    query = database_skladiste.cursor()
    query.execute('SELECT naziv, privitak FROM proizvodi WHERE privitak IS NOT NULL')
    rows = query.fetchall()
    
    query.close()
    database_skladiste.close()
    return rows

def get_product_sum():
        database_skladiste = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=db/skladiste.accdb;')
        query = database_skladiste.cursor()
        
        query.execute('SELECT cijena * kolicina AS total_value FROM proizvodi')
        rows = query.fetchall()
        
        query.close()
        database_skladiste.close()
        
        # rows contains data like this [(45, ), (70, ), (250, ), (154, )]
        # extract and save only values from tuple and sum them
        sum = 0
        for x in rows:
            for y in x:
                sum += y
        
        return sum


###############################
''' testni dio za funkcije'''
###############################

if __name__ == "__main__":
    # print(get_product_data())
    # print(get_master_detail_data())
    # print(get_image_for_pdf())
    print(get_product_sum())