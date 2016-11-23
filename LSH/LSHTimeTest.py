import csv
import pandas
import numpy
import random
import time
from CWHashingFamily import CWHashingFamily

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

R = 4
B = 8
TEXT = 9
SHINGLES_LEN = 4
PRIME = 997
BINS = 900

def shingles(text, shingleSize):
    return [text[i:i+shingleSize] for i in xrange(0,len(text)-(shingleSize+1))]


def minhash(shinglesList, seed):
    random.seed(seed)
    minhash = -1
    for shingle in shinglesList:
        cwFactory = CWHashingFamily(BINS, PRIME)
        numericHash = cwFactory.numericFunction(random.randrange(1,PRIME), random.randrange(0,PRIME))
        stringHash = cwFactory.stringFunction(random.randrange(0,PRIME),numericHash)
        shHash = stringHash.hash(shingle)
        if ((minhash == -1) or (shHash < minhash)):
            minhash = shHash
    return minhash

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


def timeLSH():
    copy(20000)
    sentences = open("sentences.csv","r")
    sentencesCsv = csv.reader(sentences)
    start_time = time.time()
    i = 0
    for sentence in sentencesCsv:
        shList = shingles(sentence[TEXT],SHINGLES_LEN)
        minhash(shList, i)
        i += 1
    print("--- %s seconds ---" % (time.time() - start_time))
    print "Reviews:"+str(i)
    sentences.close()

timeLSH()
