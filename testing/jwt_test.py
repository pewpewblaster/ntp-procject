import jwt

# Example JWT token (this is just a sample, not a real token)
jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

# Secret key (this is just a sample, you should use a real secret key)
secret_key = "mysecretkey"

# Decode the JWT token
try:
    decoded_payload = jwt.decode(jwt_token, secret_key, algorithms=["HS256"])
    print(decoded_payload)
except jwt.InvalidSignatureError as e:
    print("Invalid JWT signature. Token may have been tampered with.")
    print("Error details:", e)
except jwt.ExpiredSignatureError as e:
    print("JWT token has expired.")
    print("Error details:", e)
except jwt.DecodeError as e:
    print("Error decoding JWT token.")
    print("Error details:", e)
except jwt.InvalidTokenError as e:
    print("Invalid JWT token.")
    print("Error details:", e)
    
#print(decoded_payload)
