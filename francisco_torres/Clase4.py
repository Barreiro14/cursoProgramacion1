import csv
import numpy as np
import matplotlib.pyplot as plt




def GetData(i):
    with open('iqporpaises.csv', 'r') as file:
        data = []
        reader = csv.reader(file)
        next(reader)
    
        for row in reader:
           data.append(float(row[i]))
        return data





iq = 2
pop2020 = 3
dataiq = np.array(GetData(iq))
datapop = np.array(GetData(pop2020))

#Organizando los valores en la data
mydict = dict(zip(datapop, dataiq))

sorted_dict = dict(sorted(mydict.items()))

#Creando el grafico
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15,10))
ax1.scatter(list(sorted_dict.keys()), list(sorted_dict.values()))
ax2.scatter(list(sorted_dict.values()), list(sorted_dict.keys()))

ax1.grid()
ax2.grid()

ax1.set_xlabel('Poblacion', fontsize=15)
ax1.xaxis.set_label_coords(x=0.5, y=-0.02)
ax1.set_ylabel('IQ', fontsize=20)
ax1.set_title('Relacion poblacion - iq')

ax2.set_xlabel('IQ', fontsize=15)
ax2.set_ylabel('Poblacion', fontsize=20)
ax2.set_title('Relacion iq - poblacion')

plt.show()


	
