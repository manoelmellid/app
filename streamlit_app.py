import streamlit as st
from pages import prediccion, navegacion, flujos, ocupacion

st.set_page_config(page_title="Inicio")

col1, col2, col3 = st.columns([3,3,3])
with col1:
    st.image("amtega_logo.png_2089811488.png", use_column_width=True)
with col3:
    st.header("SMETRIA")

st.markdown("<h3 style='text-align: center;'>Universidade de Santiago de Compostela</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Grao en Intelixencia Artificial</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Proxecto Integrador I</h4>", unsafe_allow_html=True)

st.write("Este proyecto se encuadra dentro del caso de Uso \"Sistema de monitorización de eventos en los últimos tramos del Camino de Santiago\".")
st.write("Se ha desarrollado esta aplicación web que agrupa todas las funcionalidades requeridas por el caso de uso planteado por la entidad colaboradora AMTEGA.")

