import streamlit as st
from Pages import home

st.set_page_config(
    page_title="Batu Itam Perdana POS",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.linkedin.com/in/rifkyaliffa/",
        "Report a bug": "https://github.com/Penzragon",
        "About": "A Simple POS App For Batu Itam Perdana (**BIP**).",
    },
)

PAGES = {"Home": home}
st.sidebar.title("Navigation")
selection = st.sidebar.selectbox("Choose a page", list(PAGES.keys()))

page = PAGES[selection]
page.app()