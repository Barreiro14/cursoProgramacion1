
f = open("elprofeejevi.txt", "r") #TODO: Ususalmente se deja en "r" para no modificar la base de datos
#next(f)
sum = 0
is_float_found = False

def is_float(string):
    string = string.replace("\n", "")
    if string.replace(".", "").isnumeric():
        return True
    else:
        return False

with open("elprofeejevi.txt", "r") as f:
    for line in f:
        if is_float(line):
            sum += float(line)
            is_float_found = True

if is_float_found:
    print(sum)
else:
    print("No se encontraron números válidos en el archivo.")
