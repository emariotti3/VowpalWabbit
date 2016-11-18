import CarterWegman

class NumericCarterWegman(CarterWegman):

    def hash(number):
        return ((self.a*number + self.b) % self.primeNumber) % self.mBins
