import logging
import mysql.connector
import streamlit as st

from customer_operations import (
    get_all_customers,
    delete_customer
)

logger = logging.getLogger(__name__)

st.title("Restaurant Management System")

st.subheader("Customers")

customers = get_all_customers()

for customer in customers:
    st.write(customer)

st.subheader("Delete Customer")

customer_id = st.text_input(
    "Enter Customer ID"
)

if st.button("Delete"):

    try:

        delete_customer(
            customer_id
        )

    except ValueError as error:

        st.error(
            str(error)
        )

    except mysql.connector.Error:

        logger.exception(
            "Deleting customer failed"
        )

        st.error(
            "Could not delete customer. Please try again."
        )

    else:

        st.success(
            "Customer deleted successfully."
        )

        st.rerun()