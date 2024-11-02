import streamlit as st
import pandas as pd
import numpy as np
from utils import obtener_coordenadas as obcoor, pronostico as prn

def mostrar_pagina():
    st.header("Predicción meteorológica")
    if concello_id is not None:
        st.write(f"### Predicción para tu ubicación: {concello_id}")

    if latitud is not None and longitud is not None:
        # Crear el DataFrame solo si ambos valores son válidos
        data = pd.DataFrame({
            'lat': [latitud],  # Mejor como lista
            'lon': [longitud]
        }, index=[0])  # Proporciona un índice
        
        # Mostrar el mapa solo si los datos son válidos
        st.map(data)

    if adelante is not None:
        dias = 2
        prn.pronostico(ubicacion, dias)

        # Carga de los datos
        df = pd.read_csv("salida_forecast_data.csv")

        # Convertir la columna 'date_time' en un formato de fecha adecuado
        df['date_time'] = pd.to_datetime(df['date_time'])

        # Gráfica de Temperature
        st.write("### Temperatura esperada:")
        st.bar_chart(df[['date_time', 'temperature']].set_index('date_time'))

        # Gráfica de Precipitation Amount
        st.write("### Precipitaciones esperadas:")
        st.bar_chart(df[['date_time', 'precipitation_amount']].set_index('date_time'))

        # Gráfica de Wind Speed
        st.write("### Evolución del viento a lo largo del día")
        st.line_chart(df[['date_time', 'wind_speed']].set_index('date_time'))
