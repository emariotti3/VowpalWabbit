from CWHashingFamily import CWHashingFamily

class LSH:

    def __init__(self, r, b):
        self.r = r
        self.b = b
        self.groupTables = [{} for i in xrange(0, b)]
        self.lshFamily = CWHashingFamily()

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
            if (groupHashTable.hasKey(pos)):
                groupHashTable[pos].append(record.id())
            else:
                groupHashTable[pos] = [record.id()]
            

    def getAllSimilarRecords(self, record):
        #Receives a query record.
        #Returns a list with all the similar records found.
        similarRecords = []
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
            if (groupHashTable.hasKey(pos)):
                similarRecords += groupHashTable[pos]
        return similarRecords
