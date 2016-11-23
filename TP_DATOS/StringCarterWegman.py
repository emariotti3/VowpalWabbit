class StringCarterWegman:

    def __init__(self, m, p, a, numberHashFunction):
        self.mBins = m
        self.primeNumber = p
        self.hashFunction = numberHashFunction
        self.a = a

    def hash(self, text):
        result = 0
        for i in xrange(len(text)):
            result += ord(text[i])*(self.a**i)
        result = result % self.primeNumber
        return self.hashFunction.hash(result)
