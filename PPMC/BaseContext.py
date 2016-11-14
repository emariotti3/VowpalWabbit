#MAX_CHAR_SIZE = 8
#CHAR_PROBABILITY = 2 ** MAX_CHAR_SIZE + 1 #ALL 8 BIT COMBINATIONS + EOF

END = 1
BEGIN = 0

CHARACTERS = {" ":1,"a":1,"b":1,"c":1,"d":1,"e":1,"f":1,"g":1,"h":1,"i":1,"j":1,
            "k":1,"l":1,"m":1,"n":1,"o":1,"p":1,"q":1,"r":1,"s":1,"t":1,"u":1,
            "v":1,"w":1,"x":1,"y":1,"z":1}

class BaseContext(object):

    def __init__(self):
        self.seenChars = CHARACTERS

    def hasCharacter(self, character):
        return character in self.seenChars.keys()

    def getCharacterListWithExclusionPrinciple(self, contextList):
        possibleChars = self.seenChars
        for seenChar in self.seenChars.keys():
            previouslySeen = False
            previousContexts = contextList
            while (not previouslySeen) and (previousContexts != []):
                currentContext = previousContexts[0]
                if (currentContext.hasCharacter(seenChar)):
                    del possibleChars[seenChar]
                    previouslySeen = True
                previousContexts.pop(0)
        return possibleChars

    def calculateInterval(self, character, possibleChars, interval):
        try:
            escapeFrequency = len(possibleChars)
            totalFreq = escapeFrequency
            intervalLength = (interval[END] - interval[BEGIN])
            print "old interval:( "+str(interval[BEGIN])+","+str(interval[END])+")\n"
            for frequency in possibleChars.values():
                totalFreq += frequency

            if self.hasCharacter(character):
                orderedChars = sorted(possibleChars.keys())
                beginning = interval[BEGIN]

                for currentChar in orderedChars:
                    charProb = possibleChars[currentChar] / float(totalFreq)
                    if (character == currentChar):
                        end = beginning + intervalLength*charProb
                        print "new interval FOUND:( "+str(beginning)+","+str(end)+")\n"
                        return (beginning, end)
                    else:
                        beginning += intervalLength * charProb
                        print "new beginning:"+str(beginning)+"\n"
            else:
                escapeProb = escapeFrequency / float(totalFreq)
                beginning = interval[END] - (intervalLength*escapeProb)
                print "new interval on ESCAPE:( "+str(beginning)+","+str(interval[END])+")\n"
                return (beginning, interval[END])

        except ZeroDivisionError:
            return interval


    def compress(self, character, contextList, interval):
        possibleChars = self.getCharacterListWithExclusionPrinciple(contextList)
        newInterval = self.calculateInterval(character, possibleChars, interval)
        return (True, newInterval)
