import streamlit as st

def home():
    st.title('O projektu')
    st.markdown(
        """<p style="text-align: justify;">Tato stránka je vytvořena pomocí nástroje <b>Streamlit</b> a slouží jako 
        ukázková verze pro vizualizaci dat. Pomocí této platformy je možné snadno a interaktivně prezentovat datové 
        analýzy formou grafů, tabulek a dalších vizuálních prvků. Streamlit umožňuje rychlý vývoj aplikací zaměřených 
        na data a jejich efektivní sdílení s ostatními uživateli. Cílem této demonstrace je ukázat, jak lze s 
        využitím Streamlitu zpřehlednit a&nbsp;zjednodušit prezentaci analytických poznatků.</p>""",
        unsafe_allow_html=True)

    code = '''
    import streamlit as st
    
    st.title('O projektu')
    '''

    st.code(code, language='python')


def contact():

    st.title('Kontaktní informace')
    col1, col2 = st.columns(2)


    with col1:
        st.info('Luděk Reif', icon=":material/signature:")
        st.info('+420 720 116 008', icon=":material/call:")
        st.info('luipenox@gmail.com', icon=":material/mail:")

    with col2:
        st.image('assets/images/luipenox.png', width=200)

car_accidents = st.Page(
    "analysis/2025/01/page.py",
    title="Dopravní nehody (Brno)",
    icon=":material/directions_car:")

home_page = st.Page(home, title="O projektu", icon=":material/info:")
contact_page = st.Page(contact, title="Kontakt", icon=":material/import_contacts:")

account_pages = [home_page, contact_page]

page_dict = {'Rok 2025': [car_accidents]}

pg = st.navigation({"Informace": account_pages} | page_dict)

pg.run()
