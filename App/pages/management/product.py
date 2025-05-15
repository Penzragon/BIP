import streamlit as st
import pandas as pd

st.title("Product Management")
st.write("This is the product management page.")

data = pd.DataFrame(
    {
        "product_id": [1, 2, 3, 4],
        "name": ["Product A", "Product A", "Product B", "Product C"],
        "base_price": [10000, 100000, 20000, 30000],
        "sale_price": [12000, 120000, 22000, 32000],
        "category": ["Category 1", "Category 1", "Category 2", "Category 3"],
        "uom": ["pcs", "carton", "pcs", "pcs"],
    }
)
categories = pd.DataFrame(
    {
        "category_id": [1, 2, 3, 4, 5],
        "name": [
            "Category 1",
            "Category 2",
            "Category 3",
            "Category 4",
            "Category 5",
        ],
        "description": [
            "Description 1",
            "Description 2",
            "Description 3",
            "Description 4",
            "Description 5",
        ],
    }
)

uoms = pd.DataFrame(
    {
        "uom_id": [1, 2, 3, 4, 5],
        "name": ["pcs", "carton", "box", "kg", "gram"],
        "description": [
            "Description 1",
            "Description 2",
            "Description 3",
            "Description 4",
            "Description 5",
        ],
    }
)

product_tab, category_tab, uom_tab = st.tabs(
    ["Product List", "Category List", "UOM List"]
)
with product_tab:
    product_data_tab, add_product_tab = st.tabs(["Product Data", "Add Product"])
    with product_data_tab:
        col_filter_name, col_filter_category, col_filter_uom = st.columns([1, 1, 1])
        with col_filter_name:
            filter_name = st.text_input("Filter by Name")
        with col_filter_category:
            filter_category = st.selectbox(
                "Filter by Category", ["All", "Category 1", "Category 2", "Category 3"]
            )
        with col_filter_uom:
            filter_uom = st.selectbox("Filter by UOM", ["All", "pcs", "carton"])
        st.write("Product Data:")
        st.dataframe(
            (
                data
                if filter_name == ""
                and filter_category == "All"
                and filter_uom == "All"
                else data[
                    (data["name"].str.lower().str.contains(filter_name.lower()))
                    & (
                        data["category"] == filter_category
                        if filter_category != "All"
                        else True
                    )
                    & (data["uom"] == filter_uom if filter_uom != "All" else True)
                ]
            ),
            column_config={
                "base_price": st.column_config.NumberColumn(
                    "Base Price", format="localized", help="Base price of the product"
                ),
                "sale_price": st.column_config.NumberColumn(
                    "Sale Price", format="localized", help="Sale price of the product"
                ),
            },
            use_container_width=True,
        )
