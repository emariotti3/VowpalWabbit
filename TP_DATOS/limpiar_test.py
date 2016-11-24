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


# Archivo de salida
# Cabecera:
# "Id","ProductId","UserId","ProfileName","HelpfulnessNumerator","HelpfulnessDenominator","Time","Summary","Text"
# Reemplazar "COMILLAS" por "
cabecera = ",".join(( "Id", "ProductId", "UserId", "ProfileName", "HelpfulnessNumerator", "HelpfulnessDenominator" ,"Time", "Summary", "Text"))
textos = []
with open("test.csv") as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        summary = "COMILLAS"+limpiar_texto(row["Summary"])+"COMILLAS"
        text = "COMILLAS"+limpiar_texto(row["Text"])+"COMILLAS"
        textos.append(",".join((row["Id"], "COMILLAS"+row["ProductId"]+"COMILLAS", "COMILLAS"+row["UserId"]+"COMILLAS", "COMILLAS"+row["ProfileName"]+"COMILLAS", row["HelpfulnessNumerator"], row["HelpfulnessDenominator"],row["Time"], summary, text)))

lineas = 0
with open("test_limpio.csv", "wb") as outfile:
    outfile.write( cabecera + "\n" )
    for elemento in textos:
        outfile.write( elemento + "\n" )
        lineas += 1
        if lineas == 100000:
            print "Se escribieron 100k lineas"
            lineas = 0