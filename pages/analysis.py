import streamlit as st
from menu import menu

import pandas as pd
import altair as alt


st.set_page_config(page_title="Datová analýza", page_icon="🏠", layout="wide")


def sidebar():
    return st.sidebar.selectbox("Vyberte rok:", [2025, 2024, 2023])


def main_content(selection):
    if selection == 2025:
        st.title("Rok 2025")
        from data._2025._01_nehody_brno import page as _2025_01
        _2025_01.app()


    elif selection == "Stránka 1":
        # from pages.home import app as page1_app
        # page1_app()
        ...
    elif selection == "Stránka 2":
        # from pages.iris import app as page2_app
        # page2_app()
        ...


def app():
    menu()

    selection = sidebar()
    main_content(selection)


if __name__ == "__main__":
    app()