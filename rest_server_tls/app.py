import jwt
  # Make sure to import the jwt module
import sqlite3
import ctypes
from flask import Flask, request, jsonify
import ssl
import datetime

# Load SQLite library
sqlite3 = ctypes.CDLL('SQLite/sqlite3.dll')
import sqlite3

app = Flask(__name__)

# Secret key for JWT token encoding and decoding
SECRET_KEY = "KWTP3SZLFTepQ3kauxGyF4d8l1CbhuK1"

def get_db_connection():
    conn = sqlite3.connect("jwt_database.db")
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


# Endpoint to generate and return JWT token
@app.route('/api/get_token', methods=['GET'])
def get_token():
    username = request.headers.get('Username')
    
    if username and username == 'admin':
        
        current_datetime = datetime.datetime.now()
        timestamp = current_datetime.strftime("%Y-%m-%d-%H-%M-%S")
        
        payload = {"username": username,}
        #           "timestamp": timestamp}
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        
        # Save or update the token in the database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO users (username, jwt_token) VALUES (?, ?)", (username, token))
        conn.commit()
        conn.close()
        
        return jsonify({"jwt_token": token})
    else:
        return jsonify({"message": "Access denied. Only 'admin' can generate tokens."}), 401


# Define a resource for protected routes
@app.route('/api/protected', methods=['GET'])
def protected_resource():
    token = request.headers.get('Authorization')
    print(token)
    if not token:
        return jsonify({"message": "Token missing"}), 401
    
    try:
        return jsonify({"message": "Access granted"})
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token expired"}), 401
    except jwt.DecodeError:
        return jsonify({"message": "Token invalid"}), 401
    
if __name__ == '__main__':
    ssl_cert_path = 'cert.pem'
    ssl_key_path = 'cert-key.pem'

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=ssl_cert_path, keyfile=ssl_key_path)

    app.run(host='0.0.0.0', port=443, ssl_context=context)
