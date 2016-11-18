import logging
from BaseContext import BaseContext

END = 1
BEGIN = 0

class Context(BaseContext):

    def __init__(self, contextKey, character):
        self.key = contextKey
        self.seenChars = {}
        self.seenChars[character] = 1
        self.toAdd = ""

    def __refreshContext(self):
        if (self.toAdd == ""):
            return False
        if (super(Context,self).hasCharacter(self.toAdd)):
            self.seenChars[self.toAdd] += 1
        else:
            self.seenChars[self.toAdd] = 1
        self.toAdd = ""
        return True

    def __add(self, character):
        #adds a character to be added to context in following compression step
        self.toAdd = character

    def isContext(self,contextKey):
        return (self.key == contextKey)

    def name(self):
        return self.key

    def calculateInterval(self, character, possibleChars, interval):
        try:
            escapeFrequency = len(possibleChars)
            totalFreq = escapeFrequency
            intervalLength = (interval[END] - interval[BEGIN])
            logging.info("Old interval:( "+str(interval[BEGIN])+","+str(interval[END])+")")
            for frequency in possibleChars.values():
                totalFreq += frequency

            if self.hasCharacter(character):
                orderedChars = sorted(possibleChars.keys())
                beginning = interval[BEGIN]

                for currentChar in orderedChars:
                    charProb = possibleChars[currentChar] / float(totalFreq)
                    if (character == currentChar):
                        end = beginning + intervalLength*charProb
                        logging.info("New interval FOUND:("+str(beginning)+","+str(end)+")")
                        return (beginning, end)
                    else:
                        beginning += intervalLength * charProb
            else:
                escapeProb = escapeFrequency / float(totalFreq)
                beginning = interval[END] - (intervalLength*escapeProb)
                logging.info("New interval on ESCAPE at context "+str(self.key)+":( "+str(beginning)+","+str(interval[END])+")")
                return (beginning, interval[END])

        except ZeroDivisionError:
            logging.exception("Divided by zero at context: " + str(self.key) + "." + str(e))
            return interval


    def compress(self, character, contextList, interval):
        try:
            self.__refreshContext()
            logging.info( "Context "+self.key+" to compress: "+character+ " with "+str(self.seenChars))
            newInterval = interval
            compressed = (character in self.seenChars.keys())

            possibleChars = super(Context,self).getCharacterListWithExclusionPrinciple(contextList)
            newInterval = self.calculateInterval(character, possibleChars, interval)

            self.__add(character)

            contextList.append(self)
            return (compressed, newInterval)
        except Exception, e:
            logging.exception( 'Exception in context'+str(self.key)+': '+ str(e))
            return (False, interval)
