import random

class VectorCarterWegman():

    def __init__(self, m, p, a):
        #Returns an instance of VectorCarterWegman, which
        #represents a Carter-Wegman function for vectors.
        self.primeNumber = p
        self.mBins = m
        self.a = a


    def hash(vector):
        hashVal = 0
        coefficient = 1
        random.seed(self.seed)
        for x in vector:
            coefficient = random.randrange(1,self.mBins)
            hashVal += (x*coefficient) % self.primeNumber
        return hashVal % self.mBins
