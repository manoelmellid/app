import pandas as pd

def query_csv_data(km_value):
    # Cargar el archivo CSV
    df = pd.read_csv('vertices_250_camino_pt.csv')  # Asegúrate de que la ruta sea correcta
    
    # Filtrar los datos donde la columna 'km' es igual a km_value
    filtered_df = df[df['km'] == km_value][['longitud', 'latitud', 'concello_id', 'ubicacion']]
    
    # Extraer las columnas como listas
    longitud = filtered_df['longitud'].tolist()
    latitud = filtered_df['latitud'].tolist()
    concello_id = filtered_df['concello_id'].tolist()
    ubicacion = filtered_df['ubicacion'].tolist()

    # Retornar las listas
    return longitud, latitud, concello_id, ubicacion
