import streamlit as st
from pages import inicio, prediccion, navegacion, flujos, ocupacion

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
    navegacion.mostrar_pagina()
elif pagina == "Modelo predictivo de flujos (BETA)":
    flujos.mostrar_pagina()
elif pagina == "Modelo predictivo de ocupación (BETA)":
    ocupacion.mostrar_pagina()
