import streamlit as st
from menu import menu

import pandas as pd
import altair as alt



st.set_page_config(page_title="Úvod", page_icon="🏠", layout="wide")

menu()

def app():
    st.title("Stránka 2")
    st.write("Toto je obsah druhé stránky.")

    st.title("Barový graf - příklad")

    # Umělá data pro barový graf
    data = pd.DataFrame({
        'Kategorii': ['A', 'B', 'C', 'D'],
        'Hodnota': [10, 20, 30, 40]
    })

    # Vytvoření barového grafu
    chart = alt.Chart(data).mark_bar().encode(
        x='Kategorii',
        y='Hodnota',
        tooltip=['Kategorii', 'Hodnota']  # Zvýrazní tooltip při najetí myší
    ).properties(
        title="Barový graf ukázka"
    )

    # Zobrazení grafu ve Streamlit
    st.altair_chart(chart, use_container_width=True)

if __name__ == "__main__":
    app()