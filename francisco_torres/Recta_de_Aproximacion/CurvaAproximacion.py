import csv
import numpy as np
import matplotlib.pyplot as plt

with open("dataset.txt", "r") as f: 



    data = csv.reader(f, delimiter=" ")
    columns = list(zip(*data))
    delta = 0
    N = 0

    
    def is_float(string):
        string = string.replace('\n','')
        if string.replace('.','').isdigit():    
           return True
        else:
           return False
    #Convertir el array a float o entero en numpy    
    def make_float(arr):
    	new_arr=[]
    	for element in arr:
    	    if is_float(element):
    	       new_arr.append(float(element))
    	arr=np.array(new_arr)
    	return arr


    x_values = make_float(columns[0])
    y_values = make_float(columns[1])
    
    xsum = x_values.sum()
    ysum = y_values.sum()
    xysum = (x_values*y_values).sum()
    
    xsquared = (x_values**2).sum()
    	

    N = float(np.size(x_values))
    delta = N*xsquared - xsum**2
    
    A = (xsquared * ysum - xsum * xysum)/delta
    B = (N * xysum - xsum * ysum)/delta
    
    Y = A + B*x_values
    
    fig, ax = plt.subplots()
    ax.plot(x_values, Y, color='red', label = "Recta de aproximacion")
    ax.scatter(x_values, y_values, label= "Valores del dataset")
    ax.legend()
    plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

