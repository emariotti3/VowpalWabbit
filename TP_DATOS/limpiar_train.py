import re
import csv

def clean(s):
    return " ".join(re.findall(r'\w+', s,flags = re.UNICODE | re.LOCALE)).lower()

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def borrar_URL(texto):
    texto = texto.lower()
    texto = re.sub(r"http\S+", "", texto)
    texto = re.sub(r"www\S+", "", texto)
    return re.sub(r"\S+.com", "", texto)

def limpiar_texto(texto):
    texto = cleanhtml(texto)
    texto = texto.replace("\"", "")
    return borrar_URL(texto)

# Buscar repetidos 
textos = {}
with open("train.csv") as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        review = clean(limpiar_texto(row['Text']))
        valor = textos.get(review, [0, set(), []])
        valor[0] += 1
        valor[1].add(int(row['Prediction']))
        valor[2].append(row['Id'])
        textos[review] = valor

items = textos.items()
borrar = []
repetidas_aborrar = 0
for elemento in items:
    if elemento[1][0] > 1:
        if len(elemento[1][1]) > 1:
            borrar += elemento[1][2]
            repetidas_aborrar += 1
        else:
            borrar += elemento[1][2][1:]
print len(borrar)
print repetidas_aborrar

borrados = {}
for elemento in borrar:
    borrados[elemento] = None
print len(borrados)

# Archivo de salida
# Cabecera:
# "Id","ProductId","UserId","ProfileName","HelpfulnessNumerator","HelpfulnessDenominator","Prediction","Time","Summary","Text"
# Reemplazar "COMILLAS" por "
cabecera = ",".join(( "Id", "ProductId", "UserId", "ProfileName", "HelpfulnessNumerator", "HelpfulnessDenominator" ,"Prediction", "Time", "Summary", "Text"))
textos = []
with open("train.csv") as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        if row['Id'] not in borrados:
            summary = "COMILLAS"+limpiar_texto(row["Summary"])+"COMILLAS"
            text = "COMILLAS"+limpiar_texto(row["Text"])+"COMILLAS"
            textos.append(",".join((row["Id"], "COMILLAS"+row["ProductId"]+"COMILLAS", "COMILLAS"+row["UserId"]+"COMILLAS", "COMILLAS"+row["ProfileName"]+"COMILLAS", row["HelpfulnessNumerator"], row["HelpfulnessDenominator"], row["Prediction"],row["Time"], summary, text)))

lineas = 0
with open("train_sin_repeticiones.csv", "wb") as outfile:
    outfile.write( cabecera + "\n" )
    for elemento in textos:
        outfile.write( elemento + "\n" )
        lineas += 1
        if lineas == 100000:
            print "Se escribieron 100k lineas"
            lineas = 0