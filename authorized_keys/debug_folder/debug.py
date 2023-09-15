from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# Function to generate and save RSA keys
def generate_and_save_keys(private_key_path, public_key_path):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    public_key = private_key.public_key()

    # Serialize and save the private key
    with open(private_key_path, "wb") as private_key_file:
        private_key_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        private_key_file.write(private_key_pem)

    # Serialize and save the public key
    with open(public_key_path, "wb") as public_key_file:
        public_key_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        public_key_file.write(public_key_pem)

# Function to load a private key
def load_private_key(private_key_path):
    with open(private_key_path, "rb") as private_key_file:
        private_key_pem = private_key_file.read()
        private_key = serialization.load_pem_private_key(
            private_key_pem,
            password=None,
            backend=default_backend()
        )
    return private_key

# Function to load a public key
def load_public_key(public_key_path):
    with open(public_key_path, "rb") as public_key_file:
        public_key_pem = public_key_file.read()
        public_key = serialization.load_pem_public_key(
            public_key_pem,
            backend=default_backend()
        )
    return public_key

# Example usage
private_key_path = "private_key.pem"
public_key_path = "public_key.pem"

# generate_and_save_keys(private_key_path, public_key_path)

loaded_private_key = load_private_key(private_key_path)
loaded_public_key = load_public_key(public_key_path)

# You can now use the loaded_private_key and loaded_public_key for signing and verification.
