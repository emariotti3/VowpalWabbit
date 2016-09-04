import csv
import re

location_train = "train.csv"
location_test = "test.csv"

location_train_vw = "train.vw" #will be created
location_test_vw = "test.vw" #will be created

#fieldnames = ['Id', 'ProductId', 'UserId', 'ProfileName', 'HelpfulnessNumerator', 'HelpfulnessDenominator', 'Prediction', 'Time', 'Summary', 'Text']

#cleans a string "I'm a string!?" returns as "i m a string"
def clean(s):
  return " ".join(re.findall(r'\w+', s,flags = re.UNICODE | re.LOCALE)).lower()

#crea vw desde un csv
def to_vw(location_input_file, location_output_file, test = False):
    print "\nReading:",location_input_file,"\nWriting:",location_output_file
    with open(location_input_file) as infile, open(location_output_file, "wb") as outfile:
    #create a reader to read train file
        reader = csv.DictReader(infile)
        for row in reader:
            if test:
                label = "1"
            else:
                label = str(int(row['Prediction']))
            phrase = clean(row['Text'])
            summary = clean(row['Summary'])
            utilidad = '0.5'
            if float(row['HelpfulnessDenominator']) != 0:
                utilidad = str(float(row['HelpfulnessNumerator']) / float(row['HelpfulnessDenominator']))
            product_id = str(row['ProductId'])
            outfile.write(   label + 
            " '" + row['Id'] + 
            " |t " + 
            phrase +
            " |s " +
            summary +
            " |u " + 
            utilidad +
            " |p " +
            product_id +
            " |c " +
            "word_count:"+str(phrase.count(" ")+1)
            + "\n" )

to_vw(location_train, location_train_vw)
to_vw(location_test, location_test_vw, test=True)