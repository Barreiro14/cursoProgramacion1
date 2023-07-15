import math

def calculo_promedio(lista):
    total = sum(lista)
    promedio = total / len(lista)
    return promedio

def calculo_desviacion_estandar(lista):
    promedio = calculo_promedio(lista)
    suma_cuadrados = sum((x - promedio) ** 2 for x in lista)
    variacion = suma_cuadrados / len(lista)
    desviacion_estandar = math.sqrt(variacion)
    return desviacion_estandar

archivo = open("iq.txt", "r")

datos = archivo.readlines()
iq = [float(iq.strip()) for iq in datos if iq.strip().replace('.', '', 1).isdigit()]

archivo.close()

desviacion_iq = calculo_desviacion_estandar(iq)

print("La desviación estándar de los IQ de los países es:", desviacion_iq)
