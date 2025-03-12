import streamlit as st

def menu():
    st.sidebar.page_link("app.py", label="Úvod")
    st.sidebar.page_link("pages/analysis.py", label="Datová analýza")