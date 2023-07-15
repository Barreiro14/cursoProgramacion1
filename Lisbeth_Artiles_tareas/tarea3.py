import matplotlib.pyplot as plt

try:
    with open("iq.txt", "r") as f, open("pop.txt", "r") as e:
        iq_data = f.readlines()
        pop_data = e.readlines()

        iq = [float(line.strip()) for line in iq_data if line.strip().replace('.', '', 1).isdigit()]
        pop = [pop.strip().replace("'", '') for pop in pop_data[:len(iq)]]
except IOError:
    print("Error: Unable to read the data files.")

plt.plot(pop, iq)
plt.xlabel('Poblacion')
plt.ylabel('IQ')
plt.title('IQ Promedio en función de la poblacion')

plt.show()
