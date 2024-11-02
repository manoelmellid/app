import streamlit as st
import pandas as pd
import numpy as np
from utils import obtener_coordenadas as obcoor, pronostico as prn

def show():
    st.header("Modelo predictivo de flujos")
    # Aquí incluirías todo el código específico para la predicción
    
    # Función para mostrar la página de inicio
    def pagina_inicio():
        st.title("Página de Inicio")
        st.button("Ir a Turismo", on_click=lambda: cambiar_pagina("turismo"))
        st.button("Ir a Compra", on_click=lambda: cambiar_pagina("compra"))
    
    # Función para mostrar la página de turismo
    def pagina_turismo():
        st.title("Página de Turismo")
        st.button("Ir a Inicio", on_click=lambda: cambiar_pagina("inicio"))
        st.button("Ir a Compra", on_click=lambda: cambiar_pagina("compra"))
    
    # Función para mostrar la página de compra
    def pagina_compra():
        st.title("Página de Compra")
        st.button("Ir a Inicio", on_click=lambda: cambiar_pagina("inicio"))
        st.button("Ir a Turismo", on_click=lambda: cambiar_pagina("turismo"))
    
    # Función para cambiar la página
    def cambiar_pagina(pagina):
        st.session_state.pagina_actual = pagina
    
    # Inicializar el estado de la sesión si no existe
    if 'pagina_actual' not in st.session_state:
        st.session_state.pagina_actual = 'inicio'
    
    # Mostrar la página correspondiente
    if st.session_state.pagina_actual == 'inicio':
        pagina_inicio()
    elif st.session_state.pagina_actual == 'turismo':
        pagina_turismo()
    elif st.session_state.pagina_actual == 'compra':
        pagina_compra()

