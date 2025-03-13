import streamlit as st

import pandas as pd
import altair as alt



st.title('Dopravní nehody')
st.subheader('Na území města Brna v letech 2018 - 2023')
st.markdown(
    f'Zdroj dat: [data.gov.cz](https://data.gov.cz/datov%C3%A1-sada?iri=https%3A%2F%2Fdata.'
    f'gov.cz%2Fzdroj%2Fdatov%C3%A9-sady%2F44992785%2Ff7604237598371dd478232df3ad93ce9) *(data použita dne 13.03.2025)*')
data = pd.read_csv('./analysis/2025/01/data/nehody_celkem.csv')
data = data[data['rok'].isin(range(2019, 2024))]
data['rok'] = data['rok'].astype(str)

graf = alt.Chart(data).mark_bar().encode(
    x=alt.X('rok', title='Rok'),
    y=alt.Y('celkem', title='Počet nehod celkem')
).properties(
    title='Celkový počet nehod v letech'  # Název grafu
)
st.altair_chart(graf, use_container_width=True)

data2 = pd.read_csv('./analysis/2025/01/data/nehody_hlavni_pricina.csv')
data2 = data2[data2['rok'].isin(range(2019, 2024))]

# selected2 = st.selectbox('Příčína nehody', data2['hlavni_pricina'].unique())

graf = alt.Chart(data2).mark_bar().encode(
    x=alt.X('rok:N', title='Rok'),
    y=alt.Y('celkem', title='Počet nehod celkem'),
    # color=alt.Color('hlavni_pricina', title='Hlavní příčina'),
    # xOffset=alt.X('hlavni_pricina:N', sort=data2['hlavni_pricina'].unique().tolist()),
    color=alt.Color('hlavni_pricina:N', legend=None,
                    scale=alt.Scale(
                        domain=data2['hlavni_pricina'].unique().tolist(),  # Kategorie
                        range=['red', 'green', 'gray', 'orange', 'purple', 'brown']  # Odpovídající barvy
                    )),
    xOffset='hlavni_pricina:N',
).properties(
    title=f'Příčiny nehod v letech',
    height=600
)
st.altair_chart(graf, use_container_width=True)

cats = data2['hlavni_pricina'].unique().tolist()
colors = ['red', 'green', 'gray', 'orange', 'purple', 'brown']

col1, col2 = st.columns(2)
with col1:
    for cat, color in zip(cats[:3], colors[:3]):
        st.markdown(f"""
            <div style="padding: 5px; display: flex; align-items: center;">
                <div style="display: inline-block; width: 30px; height: 30px; background-color: {color}; border-radius: 10%; margin-right: 10px;"></div>
                <div style="display: inline-block;">{cat}</div>
            </div>
        """, unsafe_allow_html=True)

with col2:
    for cat, color in zip(cats[3:], colors[3:]):
        st.markdown(f"""
            <div style="padding: 5px; display: flex; align-items: center;">
                <div style="display: inline-block; width: 30px; height: 30px; background-color: {color}; border-radius: 10%; margin-right: 10px;"></div>
                <div style="display: inline-block;">{cat}</div>
            </div>
        """, unsafe_allow_html=True)

st.write("")
st.write("")

data3 = pd.read_csv('./analysis/2025/01/data/nehody_zraneni.csv')
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
).properties(
    title=f'{selected3} v letech'  # Název grafu
)
st.altair_chart(graf3, use_container_width=True)
