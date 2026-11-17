def validate_customer_id(customer_id):

    if not str(customer_id).strip():

        raise ValueError(
            "Customer ID cannot be empty"
        )

    if not str(customer_id).isdigit():

        raise ValueError(
            "Customer ID must be a number"
        )

    return int(customer_id)