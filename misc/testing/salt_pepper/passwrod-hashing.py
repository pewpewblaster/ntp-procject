import hashlib
from secrets import token_urlsafe
from hmac import compare_digest
import json
import random
import os

script_directory = os.path.dirname(os.path.abspath(__file__))


filename = "encripted_password.txt"
filepath = os.path.join(script_directory, filename)

peppers_file = "pepper.json"
json_file_path = os.path.join(script_directory, peppers_file)

def write_to_file(content):
    with open(filepath, 'w') as file:
        file.write(content)

def read_from_file():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_directory, filename)
    
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return None

def generate_salt():
    return token_urlsafe(20)

def generate_pepper():

    script_directory = os.path.dirname(os.path.abspath(__file__))
    json_filename = "pepper.json"
    json_path = os.path.join(script_directory, json_filename)

    with open(json_path, "r") as json_file:
        peppers = json.load(json_file)
    
    pepper = random.choice(peppers["peppers"])
    return pepper

def hash_password_sha256(input_password):
    salt = generate_salt()
    pepper = generate_pepper()
    print(pepper)
    password_hasher = hashlib.sha256()
    password_hasher.update((input_password + salt + pepper).encode('utf-8'))
    hashed_password = password_hasher.hexdigest()

    password = f"{salt}${hashed_password}"
    write_to_file(password)
    return password

def verify_password(input_password):
    password = read_from_file()
    salt, hashed_password = password.split("$")

    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)
    
    peppers_array = data["peppers"]

    for pepper in peppers_array:
        print(f"pepper: {pepper}")

        password_hasher = hashlib.sha256()
        password_hasher.update((input_password + salt + pepper).encode('utf-8'))
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
