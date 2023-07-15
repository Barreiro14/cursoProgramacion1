with open("elprofeejevi.txt", "r") as f: #TODO: Ususalmente se deja en "r" para no modificar la base de datos
#next(f)
    data = f.readlines()
    sum = 0
    i = 0
    def is_float(string):
        string = string.replace('\n','')
        if string.replace('.','').isdigit():    
           return True
        else:
           return False
        

    for line in data:
        i += 1
        if is_float(line):
           sum = sum + float(line)
        else:
           print(f'No se pudo sumar el valor en la linea {i}')

#avr = sum/198
print(f'La suma de los valores en la columna es {sum}')
#print(is_float("klk"))
#print(is_float("125584.8380"))
#print(type(data))
