import streamlit as st
from pages import prediccion, navegacion, flujos, ocupacion

st.sidebar.header("Menú de navegación")
pagina = st.sidebar.radio(
    "", ["Inicio", "Predicción meteorológica", "Herramienta de navegación (BETA)", 
         "Modelo predictivo de flujos (BETA)", "Modelo predictivo de ocupación (BETA)"]
)

st.markdown("<h3 style='text-align: center;'>Universidade de Santiago de Compostela</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Grao en Intelixencia Artificial</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Proxecto Integrador I</h4>", unsafe_allow_html=True)

st.write("Este proyecto se encuadra dentro del caso de Uso...")
st.write("Se ha desarrollado esta aplicación web que...")

if pagina == "Predicción meteorológica":
    prediccion.mostrar_pagina()
elif pagina == "Herramienta de navegación (BETA)":
    navegacion.mostrar_pagina()
elif pagina == "Modelo predictivo de flujos (BETA)":
    flujos.mostrar_pagina()
elif pagina == "Modelo predictivo de ocupación (BETA)":
    ocupacion.mostrar_pagina()
