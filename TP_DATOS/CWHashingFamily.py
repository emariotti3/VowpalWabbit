import random
from math import sqrt
from itertools import count, islice
from NumericCarterWegman import NumericCarterWegman
from VectorCarterWegman import VectorCarterWegman
from StringCarterWegman import StringCarterWegman

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

class CWHashingFamily:

    def __init__(self, m, p = 0):
        if not ( (p >= m and isPrime(p)) or (isPrime(m)) ):
            raise Exception("Invalid constructor parameters! p must be prime and larger than m!")
        self.primeNumber = p
        self.mBins = m

    def numericFunction(self, a, b):
        random.seed(a)
        coefA = random.randrange(1,self.primeNumber)
        random.seed(b)
        coefB = random.randrange(0,self.primeNumber)
        return NumericCarterWegman(self.mBins, self.primeNumber, coefA, coefB)

    def vectorFunction(self, a):
        random.seed(a)
        return VectorCarterWegman(self.mBins, self.primeNumber, random.randrange(1,self.mBins))

    def stringFunction(self, a, numberHashFunction):
        if (self.primeNumber <= (self.mBins/10)):
            raise Exception("The provided value for p is too low!")
        return StringCarterWegman(self.mBins, self.primeNumber, a, numberHashFunction)
