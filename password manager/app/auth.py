from passlib.context import CryptContext
from jose import JWSError, jwt 

SECRET_KEY = 'mysecretkey'
ALGORITHM = 'SHA256'

pwd_context = CryptContext(schemes=['argon2'], deprecated='auto')

def verify_password(plain_password, hashed_password):
    return pwd_context(plain_password, hashed_password)

def hash_password(password):
    return pwd_context.hash(password)