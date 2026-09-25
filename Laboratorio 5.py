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

# 3. Definir criterios de alerta con arrays de numpy e indexado booleano
# Extraemos las columnas como arrays de numpy
voltaje = df['voltaje_bateria_V'].to_numpy()
rssi = df['rssi_dbm'].to_numpy()

# Indexado booleano según los criterios de la consigna
alerta_bateria = voltaje < 3.5
alerta_senal = rssi < -85

# Conteo de registros que cumplen cada condición sumando los booleanos (True = 1, False = 0)
cant_alerta_bateria = np.sum(alerta_bateria)
cant_alerta_senal = np.sum(alerta_senal)

# Condición combinada (al menos una alerta) usando el operador OR lógico bit a bit (|)
alerta_cualquiera = alerta_bateria | alerta_senal
cant_alerta_cualquiera = np.sum(alerta_cualquiera)

print("\n--- Conteo de Alertas ---")
print(f"Batería baja (< 3.5 V): {cant_alerta_bateria}")
print(f"Señal débil (< -85 dBm): {cant_alerta_senal}")
print(f"Registros con al menos una alerta: {cant_alerta_cualquiera}")

# Guardamos esta máscara booleana como una nueva columna en el DataFrame 
# para que sea más fácil marcar los puntos de alerta en el gráfico del próximo paso.
df['alerta'] = alerta_cualquiera