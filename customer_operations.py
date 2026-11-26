import mysql.connector

from db import get_connection
from validation import validate_customer_id


def get_all_customers():

    connection = get_connection()
    cursor = connection.cursor()

    try:

        cursor.execute(
            "SELECT * FROM customers"
        )

        customers = cursor.fetchall()

        return customers

    except mysql.connector.Error as error:

        print(
            f"Database Error: {error}"
        )

        return []

    finally:

        cursor.close()
        connection.close()


def delete_customer(customer_id):

    customer_id = validate_customer_id(
        customer_id
    )

    connection = get_connection()
    cursor = connection.cursor()

    try:

        cursor.execute(
            """
            DELETE FROM customers
            WHERE customer_id = %s
            """,
            (customer_id,)
        )

        connection.commit()

        return True

    except mysql.connector.Error:

        connection.rollback()

        raise

    finally:

        cursor.close()
        connection.close()