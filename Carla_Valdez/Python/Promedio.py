def calculo_promedio(lista):
    total = sum(lista)
    promedio = total / len(lista)
    return promedio

archivo = open("iq.txt", "r")

datos = archivo.readlines()
iq = [float(iq.strip()) for iq in datos if iq.strip().replace('.', '', 1).isdigit()]

archivo.close()

promedio_iq = calculo_promedio(iq)

print("El IQ mundial promedio es:", promedio_iq)

