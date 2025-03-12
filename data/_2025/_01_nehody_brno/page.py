import streamlit as st
from menu import menu

import pandas as pd
import altair as alt

def app():
    data = pd.read_csv('./data/_2025/_01_nehody_brno/files/nehody_celkem.csv')
    data['rok'] = data['rok'].astype(str)



    graf = alt.Chart(data).mark_bar().encode(
        x=alt.X('rok', title='Rok'),
        y=alt.Y('celkem', title='Počet nehod celkem')
    ).properties(
        title='Celkový počet nehod v letech'  # Název grafu
    )
    st.altair_chart(graf, use_container_width=True)

    data2 = pd.read_csv('./data/_2025/_01_nehody_brno/files/nehody_hlavni_pricina.csv')
    data2['rok'] = data2['rok'].astype(str)

    selected2 = st.selectbox('Příčína nehody', data2['hlavni_pricina'].unique())

    graf = alt.Chart(data2[data2['hlavni_pricina'] == selected2]).mark_bar().encode(
        x=alt.X('rok', title='Rok'),
        y=alt.Y('celkem', title='Počet nehod celkem')
    ).properties(
        title=f'Příčina "{selected2}" v letech'  # Název grafu
    )
    st.altair_chart(graf, use_container_width=True)

    data3 = pd.read_csv('./data/_2025/_01_nehody_brno/files/nehody_zraneni.csv')
    data3['rok'] = data3['rok'].astype(str)

    volby = {
        'Lehce zraněné osoby': 'lehce_zraneni_celkem',
        'Těžce zraněné osoby': 'tezce_zraneni_celkem',
        'Usmrcené osoby': 'usmrceno_celkem'
    }

    selected3 = st.selectbox('Zranění osob', volby.keys())

    graf3 = alt.Chart(data3[['rok', volby[selected3]]]).mark_bar().encode(
        x=alt.X('rok', title='Rok'),
        y=alt.Y(volby[selected3], title='Počet případů')
    ).properties(
        title=f'{selected3} v letech'  # Název grafu
    )
    st.altair_chart(graf3, use_container_width=True)

