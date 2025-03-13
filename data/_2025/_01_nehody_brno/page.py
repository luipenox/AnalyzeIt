import streamlit as st
from streamlit import title

from menu import menu

import pandas as pd
import altair as alt


def app():
    data = pd.read_csv('./data/_2025/_01_nehody_brno/files/nehody_celkem.csv')
    data = data[data['rok'].isin(range(2019, 2024))]
    data['rok'] = data['rok'].astype(str)

    graf = alt.Chart(data).mark_bar().encode(
        x=alt.X('rok', title='Rok'),
        y=alt.Y('celkem', title='Počet nehod celkem')
    ).properties(
        title='Celkový počet nehod v letech'  # Název grafu
    )
    st.altair_chart(graf, use_container_width=True)

    data2 = pd.read_csv('./data/_2025/_01_nehody_brno/files/nehody_hlavni_pricina.csv')
    data2 = data2[data2['rok'].isin(range(2019, 2024))]

    # selected2 = st.selectbox('Příčína nehody', data2['hlavni_pricina'].unique())

    graf = alt.Chart(data2).mark_bar().encode(
        x=alt.X('rok:N', title='Rok'),
        y=alt.Y('celkem', title='Počet nehod celkem'),
        # color=alt.Color('hlavni_pricina', title='Hlavní příčina'),
        # xOffset=alt.X('hlavni_pricina:N', sort=data2['hlavni_pricina'].unique().tolist()),
        color=alt.Color('hlavni_pricina:N', legend=alt.Legend(orient='bottom', direction='vertical', columns=3),
                        scale=alt.Scale(
                            domain=data2['hlavni_pricina'].unique().tolist(),  # Kategorie
                            range=['red', 'green', 'gray', 'orange', 'purple', 'yellow']  # Odpovídající barvy
                        )),
        xOffset='hlavni_pricina:N'
    ).properties(
        title=f'Příčiny nehod v letech'  # Název grafu
    )
    st.altair_chart(graf, use_container_width=True)

    data3 = pd.read_csv('./data/_2025/_01_nehody_brno/files/nehody_zraneni.csv')
    data3 = data3[data3['rok'].isin(range(2019, 2024))]
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
        # color=alt.Color(volby[selected3], title='Typ', scale=alt.Scale(
        #     domain=['lehce_zraneni_celkem', 'tezce_zraneni_celkem', 'usmrceno_celkem'],  # Typy dat
        #     range=['#1f77b4', '#ff7f0e', '#ff7f0e']  # Barvy (modrá, oranžová)
        # ))
    ).properties(
        title=f'{selected3} v letech'  # Název grafu
    )
    st.altair_chart(graf3, use_container_width=True)
