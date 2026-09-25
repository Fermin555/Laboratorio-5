# Repositorio Github: 
# Autores: Fermin Delgado, Kevin Ulloa

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Cargar el archivo CSV con pandas, interpretando 'timestamp' como fecha y hora
df = pd.read_csv('telemetria_nodo_iot.csv', parse_dates=['timestamp'])

# Establecer 'timestamp' como el índice del DataFrame
df = df.set_index('timestamp')

# Imprimimos las primeras filas para verificar que todo se cargó correctamente
print("Datos cargados exitosamente:")
print(df.head())