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

# 4. Generar visualización temporal y marcar alertas con Matplotlib
# Creamos la figura y el primer eje
fig, ax1 = plt.subplots(figsize=(12, 6))

# Graficamos la temperatura asociada al eje izquierdo
ax1.set_xlabel('Tiempo (timestamp)')
ax1.set_ylabel('Temperatura (°C)', color='tab:orange')
ax1.plot(df.index, df['temperatura_C'], color='tab:orange', label='Temperatura')
ax1.tick_params(axis='y', labelcolor='tab:orange')

# Creamos un segundo eje y que comparte el mismo eje x (el tiempo)
ax2 = ax1.twinx()
ax2.set_ylabel('Voltaje Batería (V)', color='tab:blue')
ax2.plot(df.index, df['voltaje_bateria_V'], color='tab:blue', label='Voltaje')
ax2.tick_params(axis='y', labelcolor='tab:blue')

# Extraemos solo las filas donde la columna 'alerta' es True
df_alertas = df[df['alerta']]

# Superponemos puntos rojos en esos instantes específicos para señalar las alertas
ax2.scatter(df_alertas.index, df_alertas['voltaje_bateria_V'], color='red', s=50, zorder=5, label='Alerta (Bat/Señal)')

plt.title('Evolución de Temperatura y Voltaje de Batería del Nodo IoT')
fig.tight_layout() # Ajusta los márgenes automáticamente
plt.show()