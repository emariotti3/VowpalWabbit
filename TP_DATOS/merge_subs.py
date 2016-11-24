import csv

ARCHIVO1 = "submission9.csv"
ARCHIVO2 = "euge.csv"
SALIDA = "submission_merge.csv"
CABECERA = "Id,Prediction"


ID = "Id"
PREDICTION = "Prediction"

textos = {}
with open(ARCHIVO1) as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        textos[row[ID]] = row[PREDICTION]
        
with open(ARCHIVO2) as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        if row[ID] in textos and row[PREDICTION] != '0':
            textos[row[ID]] = row[PREDICTION]
        
with open(SALIDA, "wb") as outfile:
    outfile.write( CABECERA + "\n" )
    for elemento in textos:
        outfile.write( elemento+","+textos[elemento] + "\n" )