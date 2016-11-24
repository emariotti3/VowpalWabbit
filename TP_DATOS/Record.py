class Record():

    def __init__(self, rId, prediction, minhashes):
        self.recordId = int(rId)
        self.minhashList = minhashes
        self.prediction = int(prediction)
        self.tables = {}

    def id(self):
        return self.recordId

    def minhashes(self, rangeNum, totalBuckets):
        length = len(self.minhashList) / totalBuckets
        return self.minhashList[length*rangeNum : length*rangeNum + length]
    
    #def hashTo(self, table, tablePos):
        #self.tables[table] = tablePos
        
    def getTables(self):
        return self.tables.keys()
    
    def getTablePos(self, table):
        if self.tables.has_key(table):
            return self.tables[table]
        return -1
    
    def isAt(self, table, pos):
        return self.tables.has_key(table) and (self.tables[table] == pos)
    
    def getPrediction(self):
        return self.prediction
    
    def __str__(self):
        return "("+self.recordId+","+self.minhashList+")"
