from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode, urlsafe_b64decode
import os

SECERT_KEY = os.urandom(32)
SALT = os.urandom(16)

def encrypt_data(data: str) -> str:
    backend = default_backend()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length = 32,
        salt = SALT,
        iterations = 100000,
        backend = backend
    )
    
    key = kdf.dervice(SECERT_KEY)
    token = urlsafe_b64decode(token)
    iv = token[:16]
    ct = token[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
    encryptor = cipher.encryptor()
    ct = encryptor.update(data.encode('utf-8')) + encryptor.finalize()
    return urlsafe_b64decode(iv + ct).decode('utf-8')

def decrypt_data(token: str) -> str:
    backend = default_backend()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length = 32,
        salt = SALT,
        iteration = 100000,
        backend = backend
    )

    key = kdf.derive(SECERT_KEY)
    token = urlsafe_b64decode(token)
    iv = token[:16]
    ct = token[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
    decryptor = cipher.decryptor()
    return (decryptor.update(ct) + decryptor.finalize()).decode('utf-8')