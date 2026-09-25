# Repositorio Github: git@github.com:Fermin555/Laboratorio-5.git
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

# 2. Calcular estadísticas descriptivas de cada variable numérica
# Seleccionamos solo las columnas numéricas para evitar errores
columnas_numericas = df.select_dtypes(include=[np.number])

# Calculamos media, mínimo, máximo y desvío estándar integrando pandas y numpy
estadisticas = columnas_numericas.agg([np.mean, np.min, np.max, np.std])

print("\n--- Estadísticas Descriptivas ---")
print(estadisticas)