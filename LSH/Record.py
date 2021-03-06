ID = 0
MINHASHES = 1

class Record():

    def __init__(self, record):
        self.recordId = int(record[ID])
        self.minhashList = record[MINHASHES]

    def id(self):
        return self.recordId

    def minhashes(self, rangeNum, totalBuckets):
        length = len(self.minhashList) / totalBuckets
        return self.minhashList[length*rangeNum : length*rangeNum + length]
    
    def __str__(self):
        return "("+self.recordId.encode('utf-8')+","+self.minhashList.encode('utf-8')+")"
