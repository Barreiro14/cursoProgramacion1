import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Cargar el dataset desde el archivo .txt
dataset = pd.read_csv('dataset.txt', sep=' ')

# Separar las variables predictoras y la variable objetivo
X = dataset['x'].values.reshape(-1, 1)
y = dataset['F'].values

# Crear el modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo
model.fit(X, y)

# Realizar predicciones
y_pred = model.predict(X)

# Calcular métricas de rendimiento
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f"Error cuadrático medio (MSE): {mse}")
print(f"Coeficiente de determinación (R²): {r2}")

# Graficar los puntos de datos originales
plt.scatter(X, y, color='blue', label='Datos originales')

# Graficar la línea de regresión lineal
plt.plot(X, y_pred, color='red', linewidth=2, label='Regresión lineal')

# Etiquetas y leyenda
plt.xlabel('x')
plt.ylabel('F')
plt.legend()

# Mostrar la gráfica
plt.show()
