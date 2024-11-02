import streamlit as st
from pages import inicio, prediccion, herramienta_nav, modelo_flujos, modelo_ocupacion

st.sidebar.header("Menú de navegación")
pagina = st.sidebar.radio(
    "", ["Inicio", "Predicción meteorológica", "Herramienta de navegación (BETA)", 
         "Modelo predictivo de flujos (BETA)", "Modelo predictivo de ocupación (BETA)"]
)

if pagina == "Inicio":
    inicio.mostrar_pagina()
elif pagina == "Predicción meteorológica":
    prediccion.mostrar_pagina()
elif pagina == "Herramienta de navegación (BETA)":
    herramienta_nav.mostrar_pagina()
elif pagina == "Modelo predictivo de flujos (BETA)":
    modelo_flujos.mostrar_pagina()
elif pagina == "Modelo predictivo de ocupación (BETA)":
    modelo_ocupacion.mostrar_pagina()
