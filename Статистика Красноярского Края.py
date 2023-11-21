import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Статистика Красноярского Края",
    page_icon="🌿",
)
st.divider()
sf = pd.read_csv('кк_по_годам.csv')
sf['Площадь'] = sf['Площадь'].str.replace(',', '').astype(float)
sf['Плотность населения'] = sf['Плотность населения'].str.replace(',', '').astype(float)
cd = sf[['Численность', 'Год']]
cdcd= sf[['Плотность населения', 'Год']]

st.sidebar.success("Общие статистические данные по Красноярскому Краю")


st.markdown(
    """
    # Данный график представляет собой визуализацию численности населения Красноярского Края в период 1991-2022 года.
"""
)
st.divider()
st.bar_chart(cd, x="Год", y="Численность")

st.divider()

st.markdown(
    """
    # Данный график представляет собой визуализацию плотности населения Красноярского Края в период 1992-2022 года.
"""
)

sff = pd.read_csv('краснкрай.csv')
#sff['Плотность населения'] = sff['Плотность населения'].str.replace(',', '.').astype(float)
cddd = sff[['Плотность населения', 'Год']]

st.divider()

st.bar_chart(cddd, x="Год", y="Плотность населения")
st.divider()
st.markdown(
    """
    # Данный график представляет собой визуализацию процента населения, находящегося за чертой бедности, Красноярского Края в период 1995-2022 года.
"""
)
st.divider()
cdddc = sff.loc[~sf['Год'].isin([1991, 1992, 1993]), ['Процент людей за чертой бедности', 'Год']]
st.bar_chart(cdddc, x="Год", y="Процент людей за чертой бедности")
st.divider()

