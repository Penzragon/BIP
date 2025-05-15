import streamlit as st
import pandas as pd
import datetime as dt
import time

st.title("Sales")
st.write("This is the sales page.")

salesmans = pd.DataFrame(
    {"name": ["John", "Jane", "Doe"], "status": ["active", "inactive", "active"]}
)

products = pd.DataFrame(
    {
        "name": ["Product 1", "Product 2", "Product 3"],
        "price": [10000, 20000, 30000],
        "stock": [10, 20, 30],
    }
)

customers = pd.DataFrame(
    {
        "name": ["Customer 1", "Customer 2", "Customer 3"],
        "status": ["active", "inactive", "active"],
    }
)
col_date_input, col_date = st.columns([1, 1])
with col_date_input:
    date = st.date_input("Date", dt.date.today())
with col_date:
    st.markdown(
        f"<h1 style='text-align: center;'>📅 {date.strftime('%A, %d %B %Y')}</h1>",
        unsafe_allow_html=True,
    )

data = pd.DataFrame({})

col_salesman, col_customer, col_unpaid = st.columns([1, 1, 1])
with col_salesman:
    salesman = st.selectbox("Salesman", salesmans["name"])
with col_customer:
    customer = st.selectbox("Customer", customers["name"])
with col_unpaid:
    unpaid = st.selectbox("Is It Paid?", ["Yes", "No"])

if "product_inputs" not in st.session_state:
    st.session_state["product_inputs"] = [
        {"product": "", "quantity": 1, "salesman_price": 0, "include": True}
    ]
if "show_products" not in st.session_state:
    st.session_state["show_products"] = False


if st.button("Add Product", use_container_width=True):
    if (
        "product_inputs" not in st.session_state
        or len(st.session_state["product_inputs"]) == 0
    ):
        st.session_state["product_inputs"] = []

    st.session_state["product_inputs"].append(
        {"product": "", "quantity": 1, "salesman_price": 0, "include": True}
    )
    st.session_state["show_products"] = True


if st.session_state["show_products"]:
    with st.expander("Products", expanded=True):
        for i, product_input in enumerate(st.session_state["product_inputs"]):
            cols = st.columns([0.2, 4, 2, 2])
            with cols[0]:
                st.session_state["product_inputs"][i]["include"] = st.checkbox(
                    "", value=product_input.get("include", True), key=f"include_{i}"
                )
            with cols[1]:
                selected_product = st.selectbox(
                    "Product", products["name"], key=f"product_{i}"
                )
                st.session_state["product_inputs"][i]["product"] = selected_product

            with cols[2]:
                st.session_state["product_inputs"][i]["salesman_price"] = (
                    st.number_input(
                        "Salesman Price",
                        min_value=0,
                        value=products[products["name"] == selected_product][
                            "price"
                        ].values[0],
                        key=f"salesman_price_{i}",
                    )
                )
                base_price = products[products["name"] == selected_product][
                    "price"
                ].values[0]
                salesman_price = st.session_state["product_inputs"][i]["salesman_price"]
                st.caption(
                    f"Base Price: Rp {base_price:,.0f} | Salesman Price: Rp {salesman_price:,.0f}"
                )
            with cols[3]:
                st.session_state["product_inputs"][i]["quantity"] = st.number_input(
                    "Quantity",
                    min_value=1,
                    value=product_input["quantity"],
                    key=f"quantity_{i}",
                )


if "note_input" not in st.session_state:
    st.session_state["note_input"] = ""
note = st.text_area(
    "Note",
    placeholder="Add a note here...",
    height=100,
    key="note_input",
)

# --- Show "Finish" button to toggle the review form ---
if st.button("Finish", use_container_width=True):
    if (
        "product_inputs" not in st.session_state
        or len([p for p in st.session_state["product_inputs"] if p.get("include")]) == 0
    ):
        st.warning("Please add at least one product before reviewing submission.")
    else:
        st.session_state["show_review"] = True


# --- Conditionally render the review + submit form ---
if st.session_state.get("show_review", False):
    with st.form("submit_form"):
        st.markdown("### Review Submission")
        submitted_data = pd.DataFrame(
            [
                {
                    "date": date,
                    "salesman": salesman,
                    "customer": customer,
                    "product": item["product"],
                    "quantity": item["quantity"],
                    "salesman_price": item["salesman_price"],
                    "paid": True if unpaid == "Yes" else False,
                    "note": st.session_state["note_input"],
                }
                for item in st.session_state["product_inputs"]
                if item["include"]
            ]
        )
        st.dataframe(submitted_data)

        submitted = st.form_submit_button("Submit", use_container_width=True)

    with st.spinner("Submitting..."):
        if submitted:
            time.sleep(1)
            st.success("Data submitted successfully!")
            time.sleep(1)
            st.session_state["product_inputs"] = []
            st.session_state["show_products"] = (
                False  # Hide expander until user clicks Add again
            )
            st.session_state["show_review"] = False  # Hide the review form
            st.session_state.pop("note_input", None)  # Reset note
            st.rerun()
