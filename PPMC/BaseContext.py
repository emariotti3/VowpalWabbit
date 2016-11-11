import Context.py

#MAX_CHAR_SIZE = 8
#CHAR_PROBABILITY = 2 ** MAX_CHAR_SIZE + 1 #ALL 8 BIT COMBINATIONS + EOF

CHARACTERS = {" ":1,"a":1,"b":1,"c":1,"d":1,"e":1,"f":1,"g":1,"h":1,"i":1,"j":1,
            "k":1,"l":1,"m":1,"n":1,"o":1,"p":1,"q":1,"r":1,"s":1,"t":1,"u":1,
            "v":1,"w":1,"x":1,"y":1,"z":1}

    def __init__(self):
        self.seenChars = CHARACTERS

    def hasCharacter(self, character):
        return character in self.seenChars.keys()

    def __getCharacterListWithExclusionPrinciple(self, contextList):
        possibleChars = self.seenChars
        for (seenChar in self.seenChars.keys()):
            previouslySeen = False
            previousContexts = contextList
            while ((not previouslySeen) and (previousContexts != [])):
                currentContext = previousContexts[0]
                if (currentContext.hasCharacter(seenChar)):
                    del possibleChars[seenChar]
                    previouslySeen = True
                previousContexts.pop(0)
        return possibleChars

    def __calculateInterval(self, character, possibleChars, interval):
        try:
            escapeFrequency = len(possibleChars)
            totalFreq = escapeFrequency
            intervalLength = (interval[END] - interval[BEGIN])

            for (frequency in possibleChars.values())
                totalFreq += frequency

            if (self.hasCharacter(character)):
                orderedChars = sort(possibleChars.keys())
                beginning = interval[BEGIN]

                for (currentChar in orderedChars):
                    charProb = possibleChars[currentChar] / float(totalFreq)
                    if (character == currentChar):
                        end = beginning + interval*charProb
                        return (beginning, end)
                    else:
                        beginning += intervalLength * charProb
            else:
                escapeProb = escapeFrequency / float(totalFreq)
                beginning = interval[END] - (intervalLength*escapeProb)
                return (beginning, interval[END])

        catch(ZeroDivisonError):
            return interval


    def compress(self, character, contextList, interval):
        possibleChars = self.__getCharacterListWithExclusionPrinciple(contextList)
        newInterval = self.__calculateInterval(charcter, possibleChars, interval)
        return (True, newInterval)
