
f = open("elprofeejevi.txt", "r") #TODO: Ususalmente se deja en "r" para no modificar la base de datos
sum = 0
for line in f:
    if line == "pop2022\n":
        print("na, valol")
    else:
        sum = sum + float(line)

#avr = sum/198
print(sum)
print(type(f))
