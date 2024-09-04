import pyodbc
from argon2 import PasswordHasher
import urllib
import secrets
import string

username = input("What's your username? ")
website = input("Website for password? sad")


char = string.ascii_letters + string.digits + string.punctuation

length = int(input("Length of password: "))


password = "".join(secrets.choice(char) for i in range(length))



if(any(c.islower and c.isupper) for c in password):    
    print(f"your password is, {password}")

password_hasher = PasswordHasher()

hashed_password = password_hasher.hash(password)

connection_string = (
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=tcp:passdblab.database.windows.net,1433;"
    "Database=passDB;"
    "Uid=user;"
    "Pwd=pass;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)


try:
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    print("Successfully connected to the database")
except Exception as e:
    print(f"Failed to connect to database: {e}")

def store_credentials(username, password, website):

    try:
        cursor.execute('''
        INSERT INTO credentials (username, password, website)
        VALUES (?, ?, ?)
        ''', (username, password, website))
        conn.commit()
        print("Credentials stored successfully")
    except Exception as e:
        print(f"Failed to store credentials: {e}")

if __name__ == "__main__":
    username = username
    password = password
    website = website

store_credentials(username, password, website)

cursor.close
conn.close()