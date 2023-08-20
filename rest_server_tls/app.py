import jwt
from flask import Flask, request, jsonify
import ssl
from datetime import datetime
import os, json
app = Flask(__name__)

# Secret key for JWT token encoding and decoding
SECRET_KEY = "KWTP3SZLFTepQ3kauxGyF4d8l1CbhuK1"

# Endpoint to generate and return JWT token
@app.route('/api/get_token', methods=['GET'])
def get_token():
    username = request.headers.get('Username')

    current_timestamp = datetime.now()
    timestamp = str(current_timestamp)
    
    payload = {"username": username,
                "timestamp": timestamp}
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    
    return jsonify({"jwt_token": token})



# Define a resource for protected routes
@app.route('/api/protected', methods=['GET'])
def protected_resource():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"message": "Token missing"}), 401
    
    try:
        decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        print(f"Decoded payload: {decoded_payload}")

        if decoded_payload.get('username') == 'admin':
            data_file = os.path.join("json", "app_integration_data.json")
            try:
                with open(data_file, 'r') as file:
                    data = json.load(file)
                return jsonify(data)
            except FileNotFoundError:
                return jsonify({"message": "Data file not found"}), 404
        else:
            return jsonify({"message": "Unauthorized"}), 403
    except jwt.InvalidSignatureError:
        print("Invalid JWT signature. Token may have been tampered with.")
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token expired"}), 401
    except jwt.DecodeError:
        return jsonify({"message": "Token invalid"}), 401
    except jwt.InvalidTokenError:
        print("Invalid JWT token.")
        

# returns JSON data of Logistic partners information
@app.route('/api/logistic_partners', methods=['GET'])
def logistic_partners_info():
    data_file = os.path.join("json", "logistic_data.json")
    print(f"Data file path: {data_file}")
    
    try:
        with open(data_file, 'r') as file:
            logistic_partners = json.load(file)
            print("Logistic partners info requested.")
            print(logistic_partners)
            return jsonify(logistic_partners)
    except FileNotFoundError:
        return jsonify({"message": "Data file not found"}), 404
    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
        return jsonify({"message": "Invalid JSON data"}), 500  # Adjust HTTP status code as needed

# POST endpoint to add a new logistical partner
@app.route('/api/logistic_partners', methods=['POST'])
def add_logistic_partner():
    data_file = os.path.join("json", "logistic_data.json")
    
    try:
        with open(data_file, 'r') as file:
            logistic_partners = json.load(file)

        new_partner = request.json  # Assuming you send JSON data in the request body
        logistic_partners.update(new_partner)

        with open(data_file, 'w') as file:
            json.dump(logistic_partners, file, indent=4)

        return jsonify({"message": "Logistical partner added successfully"}), 201  # Return a JSON response
    except FileNotFoundError:
        return jsonify({"message": "Data file not found"}), 404
    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
        return jsonify({"message": "Invalid JSON data"}), 500  # Adjust HTTP status code as needed

if __name__ == '__main__':
    ssl_cert_path = os.path.join("certificates", "cert.pem")
    ssl_key_path = os.path.join("certificates", "cert-key.pem")

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=ssl_cert_path, keyfile=ssl_key_path)

    #app.run(host='0.0.0.0', port=443, ssl_context=context)
    app.run(ssl_context=context)
