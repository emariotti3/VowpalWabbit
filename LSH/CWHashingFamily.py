from math import sqrt
from itertools import count, islice
import NumericCarterWegman

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))


class CWHashingFamily:

    def __init__(self, m, p = 0):
        if not ( (p > 1 and isPrime(p)) or (isPrime(m)) ):
            raise Exception("Invalid constructor parameters! p must be prime and larger than m!")
        self.prime_number = p
        self.m_bins = m

    def numericFunction(self, a):
        if (a < 1 or a >= p or b < 0 or b >= p):
            raise Exception("Invalid parameters! a and b must belong to intervals [1,p) and [0,p) respectively!")
        return NumericCarterWegman(self.m, self.p, a, b)

    def vectorFunction(self, a):
        if (a < 1 or a >= p):
            raise Exception("Invalid parameters! a must belong to interval [1,p)!")
        return VectorCarterWegman(self.m, self.p, a)
