ID = 0
MINHASHES = 1

class Record():

    def __init__(self, record):
        self.id = record[ID]
        self.minhashList = record[MINHASHES]

    def id(self):
        return self.id

    def minhashes(self, rangeNum, totalBuckets):
        length = len(self.minhashList) / totalBuckets
        return self.minhashList[length*rangeNum : length*rangeNum + length]
