import csv

def promedio_oraciones(nombre_arch):
    cant_oraciones = 0
    cant_letras = 0
    fieldnames = ['Prediction ', 'UserId', 'ProfileName', 'ProductId', 'HelpfulnessNumerator', 'HelpfulnessDenominator', 'Id', 'Time', 'Summary', 'Text']
    with open(nombre_arch, "r") as csv_arch:
        r = csv.DictReader(csv_arch, fieldnames=fieldnames)
        for row in r:
            review = row["Text"]
            for letra in review:
                if (letra == "."):
                    cant_oraciones+=1
                    cant_letras += 1
            if (letra != "."):
                cant_letras += 1
    return float(cant_letras)/cant_oraciones

promedio_oraciones("train.csv")
promedio_oraciones("test.csv")
