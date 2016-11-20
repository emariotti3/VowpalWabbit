from CWHashingFamily import CWHashingFamily

BINS = 100
PRIME = 127

class LSH:

    def __init__(self, r, b):
        self.r = r
        self.b = b
        self.groupTables = [{} for i in xrange(0, b)]
        self.lshFamily = CWHashingFamily(BINS, PRIME)

    def add(self, record):
        #Receives a record to be added to the LSH object.
        for i in xrange(1, self.b + 1):
            groupHashTable = self.groupTables[i]
            #Obtain LSH function 'b'= i from lshFamilyFunction.
            #which we will use to introduce a new value to the
            #obtainted groupHashTable.
            lshFunction = self.lshFamily.vectorFunction(i)
            #Each LSH function receives r parameters each of which corresponds
            #to a different minhash function applied to the given record.
            minhashes = record.minhashes(i, self.b)
            pos = lshFunction.hash(minhashes)
            if (groupHashTable.has_key(pos)):
                groupHashTable[pos].append(record.id())
            else:
                groupHashTable[pos] = [record.id()]
        return record

    def getAllSimilarRecords(self, record):
        #Receives a query record.
        #Returns a list with all the similar records found.
        similarRecords = []
        
        for i in xrange(0, self.b):
            groupHashTable = self.groupTables[i]
            #Obtain LSH function 'b'= i from lshFamilyFunction.
            #which we will use to introduce a new value to the
            #obtainted groupHashTable.
            lshFunction = self.lshFamily.vectorFunction(i)
            #Each LSH function receives r parameters each of which corresponds
            #to a different minhash function applied to the given record.
            minhashes = record.minhashes(i, self.b)
            pos = lshFunction.hash(minhashes)
            if (groupHashTable.has_key(pos)):
                similarRecords += groupHashTable[pos]
        return similarRecords
