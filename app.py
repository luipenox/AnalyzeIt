import streamlit as st
from menu import menu

# Nastavení aplikace
st.set_page_config(
    page_title="AnalyzeIt",
    page_icon="📊",
    layout="wide",
)




def main():
    menu()
    st.title("Vítejte v mojí Streamlit aplikaci!")
    st.write("Tato aplikace je rozdělena na více stránek.")


if __name__ == "__main__":
    main()