import streamlit as st  # type: ignore

st.set_page_config(
    page_title="POS",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.linkedin.com/in/rifkyaliffa/",
        "Report a bug": "https://github.com/Penzragon",
        "About": "A Simple POS App.",
    },
)

pages = {
    "Home": [st.Page("pages/home.py", title="🏠 Home")],
    "Sales": [
        st.Page("pages/sales/sales.py", title="💵 Sales Input"),
        st.Page("pages/sales/sales_data.py", title="💹 Sales Data"),
    ],
    "Stock": [
        st.Page("pages/stock/stock.py", title="🧾 Stock Input"),
        st.Page("pages/stock/stock_data.py", title="📤 Stock Data"),
    ],
    "Report": [
        st.Page("pages/report/daily_report.py", title="📊 Daily Report"),
        st.Page("pages/report/salesman_report.py", title="👷 Salesman Report"),
        st.Page("pages/report/customer_report.py", title="🏬 Customer Report"),
        st.Page(
            "pages/report/unpaid_customer_report.py", title="📉 Unpaid Customer Report"
        ),
    ],
    "Management": [
        st.Page("pages/management/customer.py", title="🏬 Customer"),
        st.Page("pages/management/product.py", title="📦 Product"),
        st.Page("pages/management/salesman.py", title="👤 Salesman"),
    ],
}

pg = st.navigation(pages)

pg.run()
