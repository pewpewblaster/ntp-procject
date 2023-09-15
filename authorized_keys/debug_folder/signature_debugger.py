import json
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Load the private key from the PEM file
private_key_file = "private_key.pem"
with open(private_key_file, "rb") as key_file:
    private_key = serialization.load_pem_private_key(key_file.read(), password=None, backend=default_backend())

# Serialize the data
serialized_data = "json.dumps(logistic_partners)".encode('utf-8')

# Sign the data
signature = private_key.sign(
    serialized_data,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Convert the signature to base64
signature_base64 = base64.b64encode(signature).decode('utf-8')

# Print debugging information
print("Serialized Data:", serialized_data)
print("Signature:", signature_base64)
