import streamlit as st
from pages import inicio, prediccion, navegacion, flujos, ocupacion

col1, col2, col3 = st.columns([3,3,3])
with col1:
    st.image("amtega_logo.png_2089811488.png", use_column_width=True)
with col3:
    st.header("SMETRIA")

st.sidebar.header("Menú de navegación")
pagina = st.sidebar.radio(
    "", ["Inicio", "Predicción meteorológica", "Herramienta de navegación (BETA)", 
         "Modelo predictivo de flujos (BETA)", "Modelo predictivo de ocupación (BETA)"]
)

if pagina == "Inicio":
    inicio.show()
elif pagina == "Predicción meteorológica":
    prediccion.show()
elif pagina == "Herramienta de navegación (BETA)":
    navegacion.show()
elif pagina == "Modelo predictivo de flujos (BETA)":
    flujos.show()
elif pagina == "Modelo predictivo de ocupación (BETA)":
    ocupacion.show()
