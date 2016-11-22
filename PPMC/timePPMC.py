import time
import csv
from PPMC import PPMC

TEXT = 9

def copy(numSentences):
    try:
        train = open("train_sin_repeticiones.csv","r")
        out = open("sentences.csv","w")
        trainCsv = csv.reader(train)
        outCsv = csv.writer(out)

        for i in xrange(numSentences):
            outCsv.writerow(trainCsv.next())

        train.close()
        out.close()
    except Exception,e:
        print str(e)


def timePPMC():
    ppmc = PPMC(4, None)
    copy(20000)
    sentences = open("sentences.csv","r")
    sentencesCsv = csv.reader(sentences)
    start_time = time.time()
    for sentence in sentencesCsv:
        ppmc.compress(sentence[TEXT])
    print("--- %s seconds ---" % (time.time() - start_time))
    sentences.close()

timePPMC()
