import streamlit as st
from pages import prediccion, navegacion, flujos, ocupacion

st.set_page_config(page_title="Inicio")

col1, col2, col3 = st.columns([3,3,3])
with col1:
    st.image("amtega_logo.png_2089811488.png", use_column_width=True)
with col3:
    st.header("SMETRIA")

st.markdown("<h3 style='text-align: center;'>Sistema de monitorización de eventos en tramos</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Camino de Santiago - Camino Portugués</h3>", unsafe_allow_html=True)


st.divider()

st.write("""
El proyecto de desarrollo de esta apliación se encuadra dentro de la asignatura Proxecto Integrador I, del Grao de Intelixencia Artificial 
de la Universidade de Santiago de Compostela.
""")

st.write("""Esta aplicación cuenta con 4 funcionalidades para el usuario, un sistema de predicción meteorológica, una herramienta de consultas
geospaciales, un modelo predictivo de flujos y un modelo predictivo de ocupación
""")

