import mysql.connector
from mysql.connector import Error

# Path to your SQL file
sql_file = "alx_book_store.sql"

try:
    # Connect to MySQL server (without specifying a database)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",        # Replace with your MySQL username
        password="password" # Replace with your MySQL password
    )
    cursor = connection.cursor()

    # Read SQL file
    with open(sql_file, "r") as file:
        sql_commands = file.read().split(';')  # Split commands by semicolon

    # Execute each SQL command
    for command in sql_commands:
        command = command.strip()
        if command:  # Skip empty lines
            cursor.execute(command)
    
    print("Database 'alx_book_store' and tables created successfully!")

except Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
