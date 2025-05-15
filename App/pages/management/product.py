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

if "update_product" not in st.session_state:
    st.session_state["update_product"] = False

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
        if not st.session_state["update_product"]:
            st.markdown(
                "<h3 style='text-align: center;'>Product Data</h3>",
                unsafe_allow_html=True,
            )
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
                    "product_id": st.column_config.NumberColumn(
                        "Product ID",
                        format="localized",
                        help="Unique identifier for the product",
                    ),
                    "name": st.column_config.TextColumn(
                        "Product Name",
                        help="Name of the product",
                    ),
                    "base_price": st.column_config.NumberColumn(
                        "Base Price",
                        format="localized",
                        help="Base price of the product",
                    ),
                    "sale_price": st.column_config.NumberColumn(
                        "Sale Price",
                        format="localized",
                        help="Sale price of the product",
                    ),
                    "category": st.column_config.Column(
                        "Category",
                        help="Category of the product",
                    ),
                    "uom": st.column_config.Column(
                        "UOM",
                        help="Unit of Measure of the product",
                    ),
                },
                use_container_width=True,
            )
            if st.button(
                "Update Product",
                use_container_width=True,
                help="Switch to update mode",
            ):
                st.session_state["update_product"] = True
                st.rerun()
        else:
            st.markdown(
                "<h3 style='text-align: center;'>🚨 Update Mode 🚨</h3>",
                unsafe_allow_html=True,
            )
            st.data_editor(
                data,
                column_config={
                    "product_id": st.column_config.NumberColumn(
                        "Product ID",
                        format="localized",
                        help="Unique identifier for the product",
                    ),
                    "name": st.column_config.TextColumn(
                        "Product Name",
                        help="Name of the product",
                    ),
                    "base_price": st.column_config.NumberColumn(
                        "Base Price",
                        format="localized",
                        help="Base price of the product",
                    ),
                    "sale_price": st.column_config.NumberColumn(
                        "Sale Price",
                        format="localized",
                        help="Sale price of the product",
                    ),
                    "category": st.column_config.SelectboxColumn(
                        "Category",
                        options=categories["name"].tolist(),
                        help="Category of the product",
                    ),
                    "uom": st.column_config.SelectboxColumn(
                        "UOM",
                        options=uoms["name"].tolist(),
                        help="Unit of Measure of the product",
                    ),
                },
                use_container_width=True,
            )
            if st.button(
                "Submit Changes",
                use_container_width=True,
                help="Submit the updated product data",
            ):
                st.session_state["update_product"] = False
                st.rerun()
