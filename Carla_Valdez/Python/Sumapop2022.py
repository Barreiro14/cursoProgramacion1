import math

def suma_total(lista):
    total = sum(lista)
    return total

f = open("elprofeejevi.txt", "r")
c = f.readlines()
datos = []
for linea in c:
    try:
        numero = float(linea.strip())
        datos.append(numero)
    except ValueError:
        continue

total = suma_total(datos)
print("La suma total es:", total)


