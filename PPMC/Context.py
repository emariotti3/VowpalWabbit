ESCAPE = "ESC"
INIT_FREQUENCY = 2
END = 1
BEGIN = 0

class Context:

    def __init__(self, conextKey, character):
        self.key = contextKey
        self.seenChars = {}
        self.totalSeen = INIT_FREQUENCY
        self.seenChars[character] = 1
        self.charToAdd = ""

    def is(contextKey):
        return (self.key == contextKey)

    def hasCharacter(self, character):
        return character in self.seenChars.keys()

    def __refreshContext(self):

        if (not self.charToAdd):
            return False
        if (self.hasCharacter(self.toAdd)):
            self.seenChars[self.toAdd] += 1
        else:
            self.seenChars[self.toAdd] = 1
        self.totalSeen += 1
        self.toAdd = ""
        return True

    def __add(character):
        #adds a character to be added to context in following compression step
        self.toAdd = character

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
        try:
            self.__refreshContext()
            newInterval = interval
            compressed = (character in self.seenChars.keys())

            possibleChars = self.__getCharacterListWithExclusionPrinciple(contextList)
            newInterval = self.__calculateInterval(charcter, possibleChars, interval)

            if (not self.hasCharacter(character)):
                self.__add(character)

            contextList.append(self)
            return (compressed, newInterval)
        catch(Exception):
            return (False, interval)
