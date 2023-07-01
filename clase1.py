
f = open("elprofeejevi.txt", "r") #TODO: Ususalmente se deja en "r" para no modificar la base de datos
#next(f)
sum = 0
def is_float(string):
    string.replace("\n","")
    if string.replace(".", "").isnumeric():
        return True
    else:
        return False

for line in f:
    if (is_float(line)):
        sum = sum + float(line)
    else:
        print("bue miloco")

#avr = sum/198
print(sum)
print(is_float("klk"))
print(is_float("125584.8380\n"))
print(type(f))
