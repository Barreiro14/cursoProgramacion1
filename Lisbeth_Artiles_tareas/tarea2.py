import csv

with open('iqporpaises.csv', 'r') as input_file, open('iqporpaises2.csv', 'w') as output_file:
    for line in input_file:
        line = line.replace('"', '')
        output_file.write(line)
with open('iqporpaises2.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        rank, country, iq, pop2022 = row
        if not rank:
            print(f"{country} has no rank")
        else:
            with open('archivo.txt', 'a') as output_file:
                output_file.write(f"{country}, {pop2022}, {iq}\n")
            with open('archivo1.txt', 'a') as output_file:
                output_file.write(f"{iq}\n")
with open('archivo1.txt', 'r') as file:
    lines = file.readlines()
    iq_values = [float(line.strip()) for line in lines[1:] if line.strip().isdigit()]
    average = sum(iq_values) / len(iq_values)

print(f"The average IQ is: {average}")