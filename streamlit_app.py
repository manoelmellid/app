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

st.write("""Esta aplicación cuenta con 4 funcionalidades para el usuario, un sistema de predicción meteorológica, una herramienta de consultas
geospaciales, un modelo predictivo de flujos y un modelo predictivo de ocupación
""")

if st.button("Predicción"):
    st.markdown("<meta http-equiv='refresh' content='0; url=https://smetria.streamlit.app/prediccion'>", unsafe_allow_html=True)
st.divider()

st.write("""
Esta web se a desarrollado en el marco de la asignatura Proxecto Integrador I, del Grao de Intelixencia Artificial 
de la Universidade de Santiago de Compostela.
""")

nom1, nom2, nom3 = st.columns([3,3,3])
with nom1:
    st.write("Manoel Mellid Losada")
with nom2:
    st.write("Borja Puime Rodríguez")
with nom3:
    st.write("Carolina Rey Conesa")
    
seg1, seg2, seg3 = st.columns([3,3,3])
with seg2:
    st.write("3º Intelixencia Artificial - USC")


