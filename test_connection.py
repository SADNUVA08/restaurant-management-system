import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="NewStrongPassword123!",
    database="restaurant_management"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM customers")

customers = cursor.fetchall()

for customer in customers:
    print(customer)

cursor.close()
connection.close()
