import streamlit as st
import home

st.set_page_config(
    page_title="Insurance Charges Prediction",
    page_icon="🤑",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.linkedin.com/in/rifkyaliffa/",
        "Report a bug": "https://github.com/Penzragon",
        "About": "### Simple Insurance Prediction App - Rifky Aliffa",
    },
)

PAGES = {"Home": home}
st.sidebar.title("Navigation")
selection = st.sidebar.selectbox("Choose a page", list(PAGES.keys()))

page = PAGES[selection]
page.app()