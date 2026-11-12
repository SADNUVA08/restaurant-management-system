from customer_operations import get_all_customers

print("Restaurant Management System")

customers = get_all_customers()

for customer in customers:
    print(customer)
    