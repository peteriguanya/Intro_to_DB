import mysql.connector
from mysql.connector import Error
import getpass

# Ask for MySQL credentials
user = input("Enter your MySQL username: ")
password = getpass.getpass("Enter your MySQL password: ")

connection = None

try:
    # Connect to MySQL server (no database yet)
    connection = mysql.connector.connect(
        host="localhost",
        user=user,
        password=password,
        port=3307  # your MySQL port
    )

    cursor = connection.cursor()

    # Create database safely
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
    print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error: {e}")

finally:
    # Close cursor and connection safely
    if connection and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
