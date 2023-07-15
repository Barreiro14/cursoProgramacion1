import matplotlib.pyplot as plt

f = open("iq.txt", "r")
valores = f.readlines()
iq = [float(iq.strip()) for iq in valores if iq.strip().replace('.', '', 1).isdigit()]

f.close()

e = open("country.txt", "r")
datos = e.readlines()
paises = [pais.strip().replace("'", '') for pais in datos]

e.close()

plt.plot(paises, iq)
plt.xlabel('País')
plt.ylabel('IQ Promedio')
plt.title('IQ Promedio en función del País')

plt.show()





    
