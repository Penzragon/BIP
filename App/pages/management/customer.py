import streamlit as st
import pandas as pd

st.title("Customer Management")
st.write("This is the customer management page.")

data = pd.DataFrame(
    {
        "customer_id": [],
        "name": [],
        "phone": [],
        "status": [],
    }
)

data_tab, update_tab = st.tabs(["Customer List", "Update Customer"])
with data_tab:
    col_filter_name, col_filter_status = st.columns([1, 1])
    with col_filter_name:
        filter_name = st.text_input("Filter by Name")
    with col_filter_status:
        filter_status = st.selectbox("Filter by Status", ["All", "Active", "Inactive"])
    st.write("Customer Data:")
    st.data_editor(
        (
            data
            if filter_name == "" and filter_status == "All"
            else data[
                (data["name"].str.lower().str.contains(filter_name.lower()))
                & (data["status"] == filter_status if filter_status != "All" else True)
            ]
        ),
        column_config={
            "status": st.column_config.SelectboxColumn(
                "Status",
                options=["Active", "Inactive"],
                help="Status of the customer",
                required=True,
            ),
        },
        use_container_width=True,
        num_rows="dynamic",
    )
