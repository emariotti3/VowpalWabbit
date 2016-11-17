class LSH:

    def __init__(self, r, b, minhashFamily):
        self.r = r
        self.b = b
        self.groupTables = [{} for i in xrange(0, b)]
        self.mhFamily = minhashFamily
        self.lshFamily = cwHashingFamily()

    def add(self, record):
        #Receives a record to be added to the LSH object.
        minhashCount = 1
        for i in xrange(1, self.b + 1):
            groupHashTable = self.groupTables[i]
            #Obtain LSH function 'b'= i from lshFamilyFunction.
            #which we will use to introduce a new value to the
            #obtainted groupHashTable.
            lshFunction = self.lshFamily.function(i)
            #Each LSH function receives r parameters each of which corresponds
            #to a different minhash function applied to the given record.
            minhashes = []
            for j in xrange(minhashCount, i*self.r + 1)
                text = record.text()
                #Obtain one minhash function:
                minhashFunction = self.mhFamily.function(j)
                #Obtain one minhash value:
                minhash = minhashFunction.hash(text)
                #Add it to the minhash list for this text:
                minhashes.append(minhash)
            pos = lshFunction.hash(minhashes)
            if (groupHashTable.hasKey(pos)):
                groupHashTable[pos].append(record)
            else:
                groupHashTable[pos] = [record]
            minhashCount += self.r

    def getAllSimilarRecords(self, record):
        #Receives a query record.
        #Returns a list with all the similar records found.
        similarRecords = []
        minhashCount = 1
        for i in xrange(1, self.b + 1):
            groupHashTable = self.groupTables[i]
            #Obtain LSH function 'b'= i from lshFamilyFunction.
            #which we will use to introduce a new value to the
            #obtainted groupHashTable.
            lshFunction = self.lshFamily.function(i)
            #Each LSH function receives r parameters each of which corresponds
            #to a different minhash function applied to the given record.
            minhashes = []
            for j in xrange(minhashCount, i*self.r + 1)
                text = record.text()
                #Obtain one minhash function:
                minhashFunction = self.mhFamily.function(j)
                #Obtain one minhash value:
                minhash = minhashFunction.hash(text)
                #Add it to the minhash list for this text:
                minhashes.append(minhash)

            pos = lshFunction.hash(minhashes)
            if (groupHashTable.hasKey(pos)):
                similarRecords.append(groupHashTable[pos])
            minhashCount += self.r
        return similarRecords
