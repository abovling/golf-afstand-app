import streamlit as st
import pandas as pd
import numpy as np

st.title("Golf – Korrigeret Slaglængde")

st.markdown("Beregn hvordan **vind og temperatur** påvirker dine slaglængder.")

temperatur = st.slider("Temperatur (°C)", -5, 40, 20)
vindstyrke = st.slider("Vindstyrke (m/s)", 0.0, 15.0, 0.0, 0.5)
vindvinkel = st.slider("Vindvinkel (°)", 0, 360, 0, 10, help="0° = medvind, 180° = modvind")

køller = {
    "Driver": 230,
    "3-wood": 210,
    "5-iron": 170,
    "7-iron": 150,
    "9-iron": 125,
    "PW": 110,
    "SW": 90
}

def korrigeret_afstand(standard_længde, temperatur, vindstyrke, vindvinkel):
    temp_diff = temperatur - 20
    temp_faktor = 1 + 0.003 * temp_diff
    vind_faktor = np.cos(np.radians(vindvinkel)) * 0.01 * vindstyrke
    samlet_faktor = temp_faktor + vind_faktor
    return round(standard_længde * samlet_faktor, 1)

data = []
for kølle, længde in køller.items():
    korrigeret = korrigeret_afstand(længde, temperatur, vindstyrke, vindvinkel)
    data.append({
        "Kølle": kølle,
        "Normal længde (m)": længde,
        "Korrigeret længde (m)": korrigeret
    })

df = pd.DataFrame(data)
st.dataframe(df)
