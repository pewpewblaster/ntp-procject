import hashlib
from secrets import token_urlsafe
from hmac import compare_digest
import json
import random

filename = "encripted_password.txt"

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def read_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        return content


def generate_salt():
    return token_urlsafe(20)

def generate_pepper():
    with open("pepper.json", "r") as json_file:
        peppers = json.load(json_file)
    pepper = random.choice(peppers["peppers"])
    
    return pepper

def hash_password_sha256(input_password):
    salt = generate_salt()
    pepper = generate_pepper()
    
    password_hasher = hashlib.sha256()
    password_hasher.update((input_password + salt).encode('utf-8'))
    hashed_password = password_hasher.hexdigest()

    password = f"{salt}${hashed_password}"
    write_to_file(filename, password)
    return password

def verify_password(input_password):
    password = read_from_file(filename)
    salt, hashed_password = password.split("$")

    password_hasher = hashlib.sha256()
    password_hasher.update((input_password + salt).encode('utf-8'))
    check_hashed_password = password_hasher.hexdigest()
    
    if not compare_digest(hashed_password, check_hashed_password):
        print("Wrong password")
        return None
    
    print("Correct passwrod")
    

    

def main():

    # hash_password_sha256("kava1234")
    
    password = "kava1234"
    verify_password(password)

if __name__ == "__main__":
    main()
