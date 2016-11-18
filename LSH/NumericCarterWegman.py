class NumericCarterWegman():
    
    def __init__(self, m, p, a, b):
        self.primeNumber = p
        self.mBins = m
        self.a = a
        self.b = b
    
    def hash(number):
        return ((self.a*number + self.b) % self.primeNumber) % self.mBins
