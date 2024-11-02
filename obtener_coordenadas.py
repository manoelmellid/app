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

km_value = 5  # Cambia este valor al valor de Km que deseas consultar

# Llamar a la función y asignar los resultados a las variables
longitud, latitud, concello_id, ubicacion = query_csv_data(km_value)

# Imprimir los resultados
print("Longitudes:", longitud)
print("Latitudes:", latitud)
print("Concello IDs:", concello_id)
print("Ubicaciones:", ubicacion)
