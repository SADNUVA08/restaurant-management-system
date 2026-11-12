from db import get_connection

def get_all_customers():
    connection = get_connection()

    cursor = connection.cursor()

    try:
        cursor.execute(
            "SELECT * FROM customers"
        )

        customers = cursor.fetchall()

        return customers

    finally:
        cursor.close()
        connection.close()