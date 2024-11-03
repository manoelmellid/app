import streamlit as st
import pandas as pd
import numpy as np
from utils import obtener_coordenadas as obcoor, pronostico as prn

st.set_page_config(page_title="Modelo predictivo de flujos")

col1, col2, col3 = st.columns([3,3,3])
with col1:
    st.image("amtega_logo.png_2089811488.png", use_column_width=True)
with col3:
    st.header("SMETRIA")

st.markdown("<h3 style='text-align: center;'>Sistema de monitorización de eventos en tramos</h3>", unsafe_allow_html=True)

st.divider()

st.header("Modelo predictivo de flujos")
# Aquí incluirías todo el código específico para la predicción