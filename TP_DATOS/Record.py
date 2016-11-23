ID = 0
MINHASHES = 1

class Record():

    def __init__(self, record):
        self.recordId = int(record[ID])
        self.minhashList = record[MINHASHES]
        self.tables = {}

    def id(self):
        return self.recordId

    def minhashes(self, rangeNum, totalBuckets):
        length = len(self.minhashList) / totalBuckets
        return self.minhashList[length*rangeNum : length*rangeNum + length]
    
    def hashTo(self, table, tablePos):
        self.tables[table] = tablePos
        
    def getTables(self):
        return self.tables
    
    def getTablePos(self, table):
        if self.tables.has_key(table):
            return self.tables[table]
        return -1
    
    def isAt(self, table, pos):
        return self.tables.has_key(table) and (self.tables[table] == pos)
    
    def __str__(self):
        return "("+self.recordId+","+self.minhashList+")"
