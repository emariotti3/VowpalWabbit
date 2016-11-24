class Record():

    def __init__(self, rId, prediction, minhashes):
        #Receives a record id (rId), a score (prediction)
        #and a list of minhashes (minhashes)
        self.recordId = int(rId)
        self.minhashList = minhashes
        self.prediction = int(prediction)
        self.tables = {}

    def id(self):
        return self.recordId

    def minhashes(self, rangeNum, totalBuckets):
        #Returns a specific sublist of minhashes according
        #to totalBuckets which is the total amount of existing
        #minhash sublists to be considered. RangeNum indicate
        #which of those sublists will be returned-
        length = len(self.minhashList) / totalBuckets
        return self.minhashList[length*rangeNum : length*rangeNum + length]

    def hashTo(self, table, tablePos):
        #Receives a table number and a unique position
        #on that table for this record.
        self.tables[table] = tablePos

    def getTables(self):
        #Returns the list of tables where
        #the record has been hashed.
        return self.tables.keys()

    def getTablePos(self, table):
        #Given a table number, returns the assigned position
        #on that table if the record has been hashed to that table.
        #If it hasn't been hashed to that table, this
        #method will return -1.
        if self.tables.has_key(table):
            return self.tables[table]
        return -1

    def isAt(self, table, pos):
        #Receives a table number and a position number.
        #Returns True if a record has been hashed to that position
        #on that table
        return self.tables.has_key(table) and (self.tables[table] == pos)

    def getPrediction(self):
        return self.prediction

    def __str__(self):
        return "("+self.recordId+","+self.minhashList+")"
