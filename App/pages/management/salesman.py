import streamlit as st
import pandas as pd

st.title("Salesman Management")
st.write("This is the salesman management page.")

data = pd.DataFrame(
    {
        "salesman_id": [1, 2, 3],
        "name": ["John Doe", "Jane Smith", "Alice Johnson"],
        "phone": ["0812-3456-7890", "0812-3456-7891", "0812-3456-7892"],
        "status": ["Active", "Inactive", "Active"],
    }
)

data_tab, update_tab = st.tabs(["Salesman List", "Update Salesman"])
with data_tab:
    col_filter_name, col_filter_status = st.columns([1, 1])
    with col_filter_name:
        filter_name = st.text_input("Filter by Name")
    with col_filter_status:
        filter_status = st.selectbox("Filter by Status", ["All", "Active", "Inactive"])
    st.write("Salesman Data:")
    st.dataframe(
        (
            data
            if filter_name == "" and filter_status == "All"
            else data[
                (data["name"].str.lower().str.contains(filter_name.lower()))
                & (data["status"] == filter_status if filter_status != "All" else True)
            ]
        ),
        use_container_width=True,
    )
with update_tab:
    st.write("This is the update salesman page.")
