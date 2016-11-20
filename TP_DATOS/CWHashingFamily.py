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
        if (a < 1 or a >= self.primeNumber or b < 0 or b >= self.primeNumber):
            raise Exception("Invalid parameters! a and b must belong to intervals [1,p) and [0,p) respectively!")
        return NumericCarterWegman(self.mBins, self.primeNumber, a, b)

    def vectorFunction(self, a):
        if (a < 1 or a >= self.primeNumber):
            raise Exception("Invalid parameters! a must belong to interval [1,p)!")
        return VectorCarterWegman(self.mBins, self.primeNumber, a)

    def stringFunction(self, a, numberHashFunction):
        if (self.primeNumber <= (self.mBins/10)):
            raise Exception("The provided value for p is too low!")
        return StringCarterWegman(self.mBins, self.primeNumber, a, numberHashFunction)
