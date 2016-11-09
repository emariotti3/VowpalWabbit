ESCAPE = "ESC"
INIT_FREQUENCY = 2

class Context:

    def __init__(self, conextKey, character):
        self.key = contextKey
        self.seenChars = {}
        self.totalSeen = INIT_FREQUENCY
        self.seenChars[ESCAPE] = 1
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
            self.seenChars[ESCAPE] += 1
            self.totalSeen += 1
        self.totalSeen += 1
        self.toAdd = ""
        return True

    def __add(character):
        #adds a character to be added to context in following compression step
        self.toAdd = character

    def tryCompress(self, character, contextList, interval):
        #Recives a character to be compressed a contextList whiche is a list of all the contexts
        #that have tried to compress this character and an interval which is a tuple
        #that contains the current compression interval.

        #Returns a tuple that contains the new values for the interval if compression
        #was successful.
        #If compression was not successful, the initial interval will not be modified.
        #This method will also add the character to the list of seen characters,
        #so there is no need to add it manually.

        #In either case this context will add itself to the list of contexts that
        #have tried to compress.
        try:
            self.__refreshContext()
            contextList.append(self)
            newInterval = interval

            if (self.hasCharacter(character))
                totalSeenWithContext = self.totalSeen
                for (seenChar in self.seenChars):
                    previouslySeen = False
                    previousContexts = contextList
                    while ((not previouslySeen) and (previousContexts != [])):
                        currentContext = previousContexts[0]
                        if (context.hasCharacter(seenChar)):
                            totalSeenWithContext -= 1
                            previouslySeen = True
                        previousContexts.pop(0)

                compressionProb = self.seenChars[character] / totalSeenWithContext
                newInterval = interval #TODO: calculate new interval!!!

            self.__add(character)
            return newInterval

        catch(Exception):
            return interval
