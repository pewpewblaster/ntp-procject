import hashlib
from secrets import token_urlsafe
from hmac import compare_digest
import json
import random
import os
from salt_pepper.rsa_fernet import encrypt_json, decrypt_json

script_directory = os.path.dirname(os.path.abspath(__file__))

# filename = "encripted_password.txt"
# filepath = os.path.join(script_directory, filename)

peppers_file = "pepper.json"
json_file_path = os.path.join(script_directory, peppers_file)

# def write_to_file(content):
#     with open(filepath, 'w') as file:
#         file.write(content)

# def read_from_file():
#     script_directory = os.path.dirname(os.path.abspath(__file__))
#     filepath = os.path.join(script_directory, filename)
    
#     try:
#         with open(filepath, 'r') as file:
#             content = file.read()
#             return content
#     except FileNotFoundError:
#         return None

def generate_salt(user_password):
    # stari nacin generiranja soli
    # return token_urlsafe(20)
    
    salt = ""
    list_ascii_chars = [ord(char) for char in user_password]
    
    for ascii_char in list_ascii_chars:
        salt += (chr(ascii_char + (len(salt) + 1)))
    
    salt = salt[::-1]
    
    return salt
    

def generate_pepper():

    script_directory = os.path.dirname(os.path.abspath(__file__))
    json_filename = "pepper.json"
    json_path = os.path.join(script_directory, json_filename)

    decrypt_json()
    
    with open(json_path, "r") as json_file:
        peppers = json.load(json_file)
    encrypt_json()
    
    pepper = random.choice(peppers["peppers"])
    return pepper

def hash_password_sha256(input_password):
    salt = generate_salt(input_password)
    pepper = generate_pepper()
    
    md5_salt = hashlib.md5()
    md5_salt.update(salt.encode('utf-8'))
    
    password_hasher = hashlib.sha256()
    password_hasher.update((input_password + md5_salt.hexdigest() + pepper).encode('utf-8'))
    hashed_password = password_hasher.hexdigest()

    return hashed_password


def verify_password(hashed_password, input_password):

    salt = generate_salt(input_password)
    
    md5_salt = hashlib.md5()
    md5_salt.update(salt.encode('utf-8'))
    
    
    decrypt_json()
    
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)
    peppers_list = data["peppers"]
    encrypt_json()

    for pepper in peppers_list:
        print(f"pepper: {pepper}")

        password_hasher = hashlib.sha256()
        password_hasher.update((input_password + md5_salt.hexdigest() + pepper).encode('utf-8'))
        check_hashed_password = password_hasher.hexdigest()
        
        if not compare_digest(hashed_password, check_hashed_password):
            print("Wrong password")
            continue
        
        print("Correct passwrod")
        return True
    return False
    
def main():

    # hash_password_sha256("kava1234")
    
    password = "kava1234"
    verify_password(password)

if __name__ == "__main__":
    main()