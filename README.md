# Password Manager

This project is a secure password manager that allows users to store usernames, passwords, and associated site information. The passwords are securely hashed using Argon2 and stored in a Microsoft Azure SQL database.

## Features

- **Password Encryption:** Utilizes Argon2 for hashing passwords, ensuring strong security.
- **Azure SQL Integration:** Connects to an Azure SQL Database for storing encrypted user credentials.
- **Organized Structure:** Modular design with separate files for main logic, encryption, and database operations.

## Files Overview

### `main.py`

This is the main entry point of the application. It handles user input, interacts with the database, and ensures the overall workflow of storing and retrieving passwords.

### `encryption.py`

This file contains the encryption logic used in the application. It includes functions for hashing passwords with Argon2 and verifying them during authentication.

### `database.py`

This file manages all database operations, including connecting to the Azure SQL database, inserting new credentials, and retrieving existing ones. It handles the SQL queries and ensures secure interaction with the database.
