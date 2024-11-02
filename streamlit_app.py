import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


# import obtener_coordenadas as obcoor
import pronostico as prn

# Inicializa las variables con None
longitud = None
latitud = None
concello_id = None
ubicacion = None
adelante = None

# Título de la aplicación

col1, col2, col3 = st.columns([3,3,3])

#with col1:
    #st.image("/Users/manoelmelide/Library/CloudStorage/OneDrive-UniversidadedeSantiagodeCompostela/3-Tercero/Primer_cuatri/Proxecto1/amtega_logo.png_2089811488.png", use_column_width=True)

st.markdown("<h1 style='text-align: center;'>Asistente predictivo del Camino de Santiago</h1>", unsafe_allow_html=True)

st.sidebar.header("Menú de navegación")

pagina = st.sidebar.radio("", ["Inicio", "Predicción meteorológica", "Herramienta de navegación", "Modelo predictivo de flujos", "Modelo predictivo de ocupación"])

if pagina == "Predicción meteorológica":
    st.header("Predicción meteorológica")
elif pagina == "Herramienta de navegación":
    st.header("Herramienta de navegación")
elif pagina == "Modelo predictivo de flujos":
    st.header("Modelo predictivo de flujos")
elif pagina == "Modelo predictivo de ocupación":
    st.header("Modelo predictivo de ocupación")

if pagina == "Predicción meteorológica" or pagina == "Herramienta de navegación":
    with st.form(key='my_form'):
        # Entradas del formulario
        input_text = st.text_input("Km del Camino donde te encuentras")
        # opcion_seleccionada = st.selectbox("Selecciona un número:", [1, 2, 3, 4, 5])
        # if opcion_seleccionada == 1:
            # days=1
        
        # Botón para enviar el formulario
        submit_button = st.form_submit_button(label='Enviar')

        # Verifica si el campo de texto no está vacío solo después de que se presiona el botón
        if submit_button:
            if input_text:
                km_camino = float(input_text.replace(',', '.'))
                n = int(km_camino)

                if n < km_camino < n + 0.25:
                    resultado = n + 0.25
                elif n + 0.25 < km_camino < n + 0.5:
                    resultado = n + 0.5
                elif n + 0.5 < km_camino < n + 0.75:
                    resultado = n + 0.75
                elif n + 0.75 < km_camino < n + 1:
                    resultado = n + 1
                else:
                    resultado = km_camino  # Si no está en ningún rango, devuelve el número original

                # Actualiza las variables con los resultados de la función
                longitud, latitud, concello_id, ubicacion = obcoor.obtener_coordenadas(resultado)
                adelante = 1
                
                # Imprimir las coordenadas
                if longitud is not None and latitud is not None:
                    st.write(f"Longitud: {longitud}")
                    st.write(f"Latitud: {latitud}")
                    st.write(f"Ahora mismo te encuentras en el concello de {concello_id}")
                    st.write(f"Ubicación: {ubicacion}")
                else:
                    st.write("No se encontraron resultados para el valor de Km proporcionado.")
            else:
                st.warning("Por favor, introduce una distancia en kilómetros.")

if pagina == "Inicio":
    st.markdown("<h3 style='text-align: center;'>Universidade de Santiago de Compostela</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Grao en Intelixencia Artificial</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Proxecto Integrador I</h4>", unsafe_allow_html=True)

    st.write("Este proyecto se encuadra dentro del caso de Uso \"Sistema de monitorización de eventos en los últimos tramos del Camino de Santiago\".")
    st.write("Se ha desarrollado esta aplicación web que agrupa todas las funcionalidades requeridas por el caso de uso planteado por la entidad colaboradora AMTEGA.")

    # Fecha de hoy
    today = datetime.today().date()

    # Fecha máxima permitida (hoy + 3 días)
    max_date = today + timedelta(days=3)

    # Selector de fecha
    date = st.date_input("Selecciona una fecha (máximo 3 días a partir de hoy)", today, max_value=max_date)

    # Mensaje de confirmación
    st.write(f"Has seleccionado la fecha: {date}")




if pagina == "Predicción meteorológica":

    if concello_id is not None:
        st.write(f"# Predicción para tu ubicación: {concello_id}")

    if latitud is not None and longitud is not None:
        # Crear el DataFrame solo si ambos valores son válidos
        data = pd.DataFrame({
            'lat': [latitud],  # Mejor como lista
            'lon': [longitud]
        }, index=[0])  # Proporciona un índice
        
        # Mostrar el mapa solo si los datos son válidos
        st.map(data)

    if adelante is not None:

        prn.pronostico(ubicacion, 1)

        # Carga de los datos
        df = pd.read_csv("/Users/manoelmelide/Documents/Meteogalicia/salida_forecast_data.csv")

        # Convertir la columna 'date_time' en un formato de fecha adecuado
        df['date_time'] = pd.to_datetime(df['date_time'])

        # Gráfica de Temperature
        st.write("### Temperatura esperada:")
        st.line_chart(df[['date_time', 'temperature']].set_index('date_time'))

        # Gráfica de Precipitation Amount
        st.write("### Precipitaciones esperadas:")
        st.bar_chart(df[['date_time', 'precipitation_amount']].set_index('date_time'))

        # Gráfica de Wind Speed
        st.write("### Evolución del viento a lo largo del día")
        st.line_chart(df[['date_time', 'wind_speed']].set_index('date_time'))

elif pagina == "Modelo predictivo de flujos":
    st.write("Aquí iría la herramienta de rutas")

elif pagina == "Herramienta de navegación":
    st.write("Aquí iría el modelo predictivo de flujos")

elif pagina == "Modelo predictivo de flujos":
    st.write("Aquí iría el modelo predictivo de ocupación")

# -----------------------