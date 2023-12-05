from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import SHA256
import base64

"""
pip3 install pycryptodome 

"""

class AESCipher:

    def __init__(self, key=None):
        """
        Initializes the AES Cipher. If a string key is provided, it is hashed to create a 32-byte key.
        """
        if isinstance(key, str):
            # Hash the key to ensure it's 32 bytes long
            self.key = SHA256.new(key.encode('utf-8')).digest()
        elif key is not None:
            # Assuming key is a byte array of length 32
            self.key = key
        else:
            # Generate a random 32-byte key
            self.key = get_random_bytes(32)

    def encrypt(self, data):
        """
        Encrypts the given data using AES-256.
        """
        cipher = AES.new(self.key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        ct = base64.b64encode(ct_bytes).decode('utf-8')
        return {'iv': iv, 'ciphertext': ct}

    def decrypt(self, enc_dict):
        """
        Decrypts the given data (provided as a dict with 'iv' and 'ciphertext') using AES-256.
        """
        iv = base64.b64decode(enc_dict['iv'])
        ct = base64.b64decode(enc_dict['ciphertext'])
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return pt.decode('utf-8')

# Example Usage
if __name__ == "__main__":
    # Using a string as a key
    aes = AESCipher("my_secret_key")

    # Encrypt
    encrypted = aes.encrypt("Hello, World!")
    print("Encrypted:", encrypted)

    # Decrypt
    decrypted = aes.decrypt(encrypted)
    print("Decrypted:", decrypted)
