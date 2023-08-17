import os
import ctypes

class JwtDatabaseManager():

    def update_or_insert_jwt(self, database_path, dll_path, username, new_jwt):
        sqlite3DLL = ctypes.CDLL(dll_path)
        SQLITE_OPEN_READWRITE = 2
        null_ptr = ctypes.c_void_p(None)
        p_src_db = ctypes.c_void_p(None)

        DatabasePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), database_path)
        connect = sqlite3DLL.sqlite3_open_v2(DatabasePath.encode('utf-8'), ctypes.byref(p_src_db), SQLITE_OPEN_READWRITE, null_ptr)

        update_query = f"UPDATE tokens SET jwt = '{new_jwt}' WHERE username = '{username}';"
        update_result = sqlite3DLL.sqlite3_exec(p_src_db, update_query.encode('utf-8'), None, null_ptr, null_ptr)

        if update_result == 0:
            if sqlite3DLL.sqlite3_changes(p_src_db) == 0:  # No rows updated
                insert_query = f"INSERT INTO tokens (username, jwt) VALUES ('{username}', '{new_jwt}');"
                insert_result = sqlite3DLL.sqlite3_exec(p_src_db, insert_query.encode('utf-8'), None, null_ptr, null_ptr)

                if insert_result == 0:
                    print(f"JWT for username '{username}' inserted successfully.")
                else:
                    print("Error inserting JWT:", sqlite3DLL.sqlite3_errmsg(p_src_db))
            else:
                print(f"JWT for username '{username}' updated successfully.")
        else:
            print("Error updating JWT:", sqlite3DLL.sqlite3_errmsg(p_src_db))

        sqlite3DLL.sqlite3_close(p_src_db)
        
    def select_all_from_table(self, database_path, dll_path):
        def extractor(unused, num_columns, pcolumn, pcolumn_name):
            print(','.join(["''" if x is None else "'"+x.decode('utf-8')+"'" for x in pcolumn[:num_columns]]))
            return 0

        sqlite3DLL = ctypes.CDLL(dll_path)
        SQLITE_OPEN_READONLY = 1 
        null_ptr = ctypes.c_void_p(None)
        p_src_db = ctypes.c_void_p(None)

        callback_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(ctypes.c_char_p))
        callback_func = callback_type(extractor)

        DatabasePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), database_path)
        connect = sqlite3DLL.sqlite3_open_v2(DatabasePath.encode('utf-8'), ctypes.byref(p_src_db), SQLITE_OPEN_READONLY, null_ptr)
        
        select_query = b"SELECT * FROM tokens"
        connect = sqlite3DLL.sqlite3_exec(p_src_db, select_query, callback_func, null_ptr, null_ptr)

        sqlite3DLL.sqlite3_close(p_src_db)
    
db_path = "../db/jwt_database.db"
dll_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sqlite3.dll")    
class_object = JwtDatabaseManager()
class_object.select_all_from_table(db_path, dll_path)
class_object.update_or_insert_jwt(db_path, dll_path, "Matija", "Svasta")
class_object.select_all_from_table(db_path, dll_path)
