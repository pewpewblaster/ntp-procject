from cryptography.fernet import Fernet
import rsa
import json
import os

def generate_keys():
    (pubKey, privKey) = rsa.newkeys(4098)
    with open('keys/pubkey.pem', 'wb') as f:
        f.write(pubKey.save_pkcs1('PEM'))

    with open('keys/privkey.pem', 'wb') as f:
        f.write(privKey.save_pkcs1('PEM'))

    fernet_key = Fernet.generate_key()
    with open('keys/fernet.key', 'wb') as f:
        f.write(fernet_key)

    return pubKey, privKey, fernet_key

def load_keys():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    keys_directory = os.path.join(script_directory, 'keys')
    pub_key_file = os.path.join(keys_directory, 'pubkey.pem')
    priv_key_file = os.path.join(keys_directory, 'privkey.pem')
    fernet_key_file = os.path.join(keys_directory, 'fernet.key')

    with open(pub_key_file, 'rb') as f:
        pubKey = rsa.PublicKey.load_pkcs1(f.read())

    with open(priv_key_file, 'rb') as f:
        privKey = rsa.PrivateKey.load_pkcs1(f.read())

    with open(fernet_key_file, 'rb') as f:
        fernet_key = f.read()

    return pubKey, privKey, fernet_key


# RSA asymmetric encryption
# Encrypt and decrypt data using RSA public key
def encrypt_with_rsa(data, pubKey):
    encrypted_data = rsa.encrypt(data.encode('utf-8'), pubKey)
    return encrypted_data

def decrypt_with_rsa(encrypted_data, privKey):
    decrypted_data = rsa.decrypt(encrypted_data, privKey).decode('utf-8')
    return decrypted_data

# RSA asymmetric encryption and decrypt
def encrypt_with_fernet(data, fernet_key):
    fernet = Fernet(fernet_key)
    encrypted_data = fernet.encrypt(data)
    return encrypted_data

def decrypt_with_fernet(encrypted_data, fernet_key):
    fernet = Fernet(fernet_key)
    decrypted_data = fernet.decrypt(encrypted_data)
    return decrypted_data

# load, save encrypted data
def save_encrypted_data(data, file_path):
    with open(file_path, 'wb') as f:
        f.write(data)

def load_encrypted_data(file_path):
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()
    return encrypted_data

# Function to print encoded and decoded JSON content
def print_encoded_and_decoded_data():
    
    pubKey, privKey, fernet_key = load_keys()
    script_directory = os.path.dirname(os.path.abspath(__file__))
    encrypted_data_directory = os.path.join(script_directory, '')
    encrypted_data_file = os.path.join(encrypted_data_directory, 'encrypted_data.bin' )
    encrypted_data = load_encrypted_data(encrypted_data_file)
    
    decrypted_fernet_data = decrypt_with_fernet(encrypted_data, fernet_key)
    decrypted_rsa_data = decrypt_with_rsa(decrypted_fernet_data, privKey)
    
    print("RSA Encoded JSON Data:")
    print(encrypted_data)
    print("\nDecoded JSON Data:")
    print(decrypted_rsa_data)
    
    return decrypted_rsa_data

def encrypt_json():
    
    pubKey, privKey, fernet_key = load_keys()
    
    script_directory = os.path.dirname(os.path.abspath(__file__))
    json_file = os.path.join(script_directory, 'pepper.json' )
    encrypted_data_file = os.path.join(script_directory, 'encrypted_data.bin')
    
    with open(json_file, 'r') as json_file:
        data_to_encrypt = json.load(json_file)
        print(f"encript {data_to_encrypt}")
        data_to_encrypt = json.dumps(data_to_encrypt)
        encrypted_data = encrypt_with_rsa(data_to_encrypt, pubKey)
        encrypted_data = encrypt_with_fernet(encrypted_data, fernet_key)
        
        save_encrypted_data(encrypted_data, encrypted_data_file)
        

        file_name = os.path.join(script_directory, "pepper.json")
    json_file.close()
    
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"{file_name} has been deleted.")
    else:
        print(f"{file_name} does not exist.")

def decrypt_json():
    
    pubKey, privKey, fernet_key = load_keys()

    script_directory = os.path.dirname(os.path.abspath(__file__))
    encrypted_data_file = os.path.join(script_directory, 'encrypted_data.bin' )
    
    if os.path.exists(encrypted_data_file):
        encrypted_data = load_encrypted_data(encrypted_data_file)
        decrypted_fernet_data = decrypt_with_fernet(encrypted_data, fernet_key)
        decrypted_rsa_data = decrypt_with_rsa(decrypted_fernet_data, privKey)
        print(f"decript: {decrypted_rsa_data}")
        
        script_directory = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(script_directory, "pepper.json")
        with open(file_name, "w", encoding="utf-8") as json_file:
            json.dump(json.JSONDecoder().decode(decrypted_rsa_data), json_file)
        json_file.close()
        
        print(f"Data saved to pepper.json")
        
        if os.path.exists(encrypted_data_file):
            os.remove(encrypted_data_file)
            print(f"{encrypted_data_file} has been deleted.")
        else:
            print(f"{encrypted_data_file} does not exist.")
    else:
        return        

if __name__ == "__main__":
    # print_encoded_and_decoded_data()
    decrypt_json()
    #encrypt_json()
