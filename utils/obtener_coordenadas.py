import pandas as pd

def query_csv_data(km_value):
    # Cargar el archivo CSV
    df = pd.read_csv('vertices_250_camino_pt.csv')  # Asegúrate de que la ruta sea correcta

    # Filtrar los datos donde la columna 'km' es igual a km_value
    filtered_df = df[df['km'] == km_value][['longitud', 'latitud', 'concello_id', 'ubicacion']]
    
    # Verificar si el DataFrame filtrado no está vacío
    if not filtered_df.empty:
        # Retornar el primer elemento de cada columna como flotante, excepto concello_id y ubicacion
        longitud = float(filtered_df['longitud'].iloc[0])  # Convertir a float
        latitud = float(filtered_df['latitud'].iloc[0])    # Convertir a float
        concello_id = filtered_df['concello_id'].iloc[0]   # Texto
        ubicacion = filtered_df['ubicacion'].iloc[0]       # Texto
        return longitud, latitud, concello_id, ubicacion
    else:
        # Si no se encuentra el km_value, retornar None para los valores de longitud y latitud
        return None, None, None, None
