from BaseContext import BaseContext

class Context(BaseContext):

    def __init__(self, contextKey, character):
        super(Context, self).__init__()
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

    def isContext(contextKey):
        return (self.key == contextKey)

    def name(self):
        return self.key

    def compress(self, character, contextList, interval):
        try:
            self.__refreshContext()
            print "Context "+self.key+" to compress: "+character+ " with "+str(self.seenChars)+"\n"
            newInterval = interval
            compressed = (character in self.seenChars.keys())

            possibleChars = super(Context,self).getCharacterListWithExclusionPrinciple(contextList)
            newInterval = super(Context,self).calculateInterval(character, possibleChars, interval)

            if (not self.hasCharacter(character)):
                self.__add(character)

            contextList.append(self)
            return (compressed, newInterval)
        except Exception, e:
            print 'Exception in context'+str(self.key)+': '+ str(e)
            return (False, interval)
