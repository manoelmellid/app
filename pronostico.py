import requests
import json
from datetime import datetime, timedelta
import csv_json as cj
import streamlit as st

API_KEY = st.secrets["API_KEY"]
base_url = 'https://servizos.meteogalicia.gal/apiv4/getNumericForecastInfo'

def pronostico(location_id, days):
    # Parámetros de la solicitud
    start_date = datetime.now()  # Hoy
    end_date = start_date + timedelta(days=days)  # Hasta 'days' días después

    params = {
        'API_KEY': API_KEY,
        'locationIds': location_id,
        'startTime': start_date.strftime('%Y-%m-%dT%H:%M:%S'),
        'endTime': end_date.strftime('%Y-%m-%dT%H:%M:%S'),
        'lang': 'es',
        'tz': 'Europe/Madrid',
        'format': 'application/json'
    }

    # Realizar la solicitud a la API
    response = requests.get(base_url, params=params)

    # Comprobar si la respuesta es exitosa
    if response.status_code == 200:
        # Convertir a JSON y mostrar los datos
        forecast_data = response.json()
        print(f"Pronóstico para el ID {location_id} del {start_date.date()} al {end_date.date()}:")
        print(forecast_data)

        # Especifica el nombre del archivo donde se guardará el JSON
        nombre_archivo = 'forecast_data.json'

        # Guarda el diccionario en un archivo JSON
        with open(nombre_archivo, 'w') as archivo:
            json.dump(forecast_data, archivo, indent=4)

        # Convierte el JSON a CSV
        cj.json_to_csv(nombre_archivo, 'salida_forecast_data.csv')
    else:
        # En caso de error, mostrar mensaje de error
        print(f"Error: {response.status_code}")
