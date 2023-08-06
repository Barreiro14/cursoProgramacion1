import numpy as np
import matplotlib.pyplot as plt

X = []
F = []
with open("dataset.txt", "r") as archivo:
    datos = archivo.readlines()
    for linea in datos[1:]: 
        f_val, x_val = linea.strip().split()
        F.append(float(f_val))
        X.append(float(x_val))

X = np.array(X)
F = np.array(F)

a, b = np.polyfit(X, F, 1)

F_p = a * X + b

plt.scatter(X, F, label='Datos reales')
plt.plot(X, F_p, color='red', label='Regresión lineal')
plt.xlabel('X')
plt.ylabel('F')
plt.legend()
plt.show()

#Por si quiero saber cuales son los valores de A y B  :^)

#print("El valor de 'A' es :", a)
#print("El valor de 'B' es :", b)
