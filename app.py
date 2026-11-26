import logging

import mysql.connector
import streamlit as st

from customer_operations import delete_customer, get_all_customers

logger = logging.getLogger(__name__)

st.set_page_config(
    page_title="Restaurant Management System",
    page_icon="🍽️",
    layout="wide"
)

st.markdown(
    """
    <style>

    .stApp {
        background-color: #F5F5F5;
    }

    h1 {
        color: #C0392B !important;
        text-align: center;
    }

    h2, h3 {
        color: #2C3E50 !important;
    }

    p {
        color: #2C3E50 !important;
    }

    label {
        color: #2C3E50 !important;
        font-weight: 600;
    }

    [data-testid="stMetricLabel"] {
        color: #2C3E50 !important;
    }

    [data-testid="stMetricValue"] {
        color: #C0392B !important;
        font-size: 40px;
    }

    .stButton button {
        background-color: #E67E22;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        border: none;
        width: 100%;
        height: 50px;
    }

    .stButton button:hover {
        background-color: #D35400;
        color: white;
    }

    </style>
    """,
    unsafe_allow_html=True
)

customers = get_all_customers()

st.title("🍽️ Restaurant Management System")

st.write(
    "Manage customer information through the restaurant management dashboard."
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Customers",
        len(customers)
    )

with col2:
    st.metric(
        "System Status",
        "Online"
    )

st.divider()

st.subheader("Customer Management")

customer_id = st.text_input(
    "Enter Customer ID to Delete"
)

if st.button("Delete Customer"):

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

st.divider()

st.info(
    "Restaurant Customer Management Dashboard"
)