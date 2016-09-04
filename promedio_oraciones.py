import csv

def promedio_oraciones(nombre_arch):
    cant_oraciones = 0
    cant_letras = 0
    with open(nombre_arch, "r") as csv_arch:
        r = csv.DictReader(csv_arch)
        review = r["Text"]
        for letra in review:
            if (letra == "."):
                cant_oraciones+=1
            cant_letras += 1
        if (letra != "."):
            cant_letras += 1
    return float(cant_letras)/cant_oraciones
