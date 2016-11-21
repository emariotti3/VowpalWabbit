ID = 0
MINHASHES = 1

class Record():

    def __init__(self, record):
        self.recordId = record[ID]
        self.minhashList = record[MINHASHES]

    def id(self):
        return self.recordId

    def minhashes(self, rangeNum, totalBuckets):
        length = len(self.minhashList) / totalBuckets
        return self.minhashList[length*rangeNum : length*rangeNum + length]
    
    def __str__(self):
        return "("+str(self.recordId)+","+str(self.minhashList)+")"
