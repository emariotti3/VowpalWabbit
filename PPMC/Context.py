import BaseContext.py

END = 1
BEGIN = 0

class Context(BaseContext):

    def __init__(self, conextKey, character):
        self.key = contextKey
        self.seenChars = {}
        self.seenChars[character] = 1
        self.charToAdd = ""

    def __refreshContext(self):
        if (not self.charToAdd):
            return False
        if (self.hasCharacter(self.toAdd)):
            self.seenChars[self.toAdd] += 1
        else:
            self.seenChars[self.toAdd] = 1
        self.toAdd = ""
        return True

    def __add(character):
        #adds a character to be added to context in following compression step
        self.toAdd = character

    def is(contextKey):
        return (self.key == contextKey)

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
