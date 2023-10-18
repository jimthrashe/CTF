


import os
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
import base64

# Path to the ciphertext file in the same directory as the script
ciphertext_file = '/home/jamest/Documents/NCL/Practice/Cryptography/ciphertext'

# Function to derive a key from the timestamp
def derive_key(timestamp):
    password = timestamp.encode('utf-8')
    salt = os.urandom(16)  # Random salt
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=32,
    )
    return base64.urlsafe_b64encode(kdf.derive(password))

try:
    with open(ciphertext_file, 'rb') as file:
        ciphertext = file.read()

    timestamp = '2023-01-01 00:00:00'  # Replace with your timestamp
    key = derive_key(timestamp)

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    decrypted_data = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    # If decryption is successful, you can process 'decrypted_data' here
    print(f"Decryption successful with timestamp: {timestamp}")
    print(f"Decrypted data: {decrypted_data.decode('utf-8')}")

except FileNotFoundError:
    print(f"'{ciphertext_file}' not found in the current directory.")
except Exception as e:
    print(f"An error occurred: {e}")

