from Context import Context
from Model import Model
from BaseModel import BaseModel

stopWords = ["a","about","above","across","after","afterwards", "are","around","as","at","be", "because", "been",
             "for","go", "had","has", "have", "him", "his", "her", "hers", "them", "in", "on","theirs", ".", ",", "-",
             "it", "is", "was", "who", "when", "where", "which", "what", "that", "the", "there", "they", "then", "this",
             "got", "i", "an", "to", "under", "through", "of", "since", "and", "you", "get", "out", "or", "up", "down"]

PPMC_ORDER = 4 #PRESUMABLY THE "BEST" ORDER

def ppmc(text, order):
    text = text.lower()
    interval = (0,1)
    models = [BaseModel()]
    for i in xrange(0, order+1):
        models.append(Model(i))
    for pos in xrange(0, len(text)):
        compressed = False
        modelNum = order+1
        while not compressed:
            compression = models[modelNum].compress(text, pos, [], interval)
            compressed = compression[0]
            interval = compression[1]
            modelNum -= 1
    return interval

#print ppmc("ZZZAABAABAABBCCCCCCC",2)
#print ppmc("AAAAAAAAAAAAAAAAAACC",2)
print ppmc("ABCDAAAABCDEF",2)
