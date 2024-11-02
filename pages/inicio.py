import streamlit as st
from pages import prediccion, navegacion, flujos, ocupacion

def show():
    st.markdown("<h3 style='text-align: center;'>Universidade de Santiago de Compostela</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Grao en Intelixencia Artificial</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Proxecto Integrador I</h4>", unsafe_allow_html=True)
    
    st.write("Este proyecto se encuadra dentro del caso de Uso \"Sistema de monitorización de eventos en los últimos tramos del Camino de Santiago\".")
    st.write("Se ha desarrollado esta aplicación web que agrupa todas las funcionalidades requeridas por el caso de uso planteado por la entidad colaboradora AMTEGA.")

col1, col2, col3, col4 = st.columns(4)

# Colocar los botones en las columnas
with col1:
    if st.button('Predicción meteorológica'):
        prediccion.show()
with col2:
    if st.button('Herramienta de navegación (BETA)'):
        navegacion.show()
with col3:
    if st.button('Modelo predictivo de flujos (BETA)'):
        flujos.show()
with col4:
    if st.button('Modelo predictivo de ocupación (BETA)'):
        ocupación.show()
