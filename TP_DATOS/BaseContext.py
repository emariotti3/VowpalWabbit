import logging

END = 1
BEGIN = 0
CTX_NAME = "BASE CONTEXT"

CHARACTERS = {" ":1,"a":1,"b":1,"c":1,"d":1,"e":1,"f":1,"g":1,"h":1,"i":1,"j":1,
            "k":1,"l":1,"m":1,"n":1,"o":1,"p":1,"q":1,"r":1,"s":1,"t":1,"u":1,"v":1,
            "w":1,"x":1,"y":1,"z":1, ".": 1, ",":1, "'":1, "!":1, "?":1,"-":1, "/":1,
            "*":1, "+":1, ":":1, "%":1,"$":1, "#":1, "&":1,"(":1, ")":1, "=":1,">":1,
            ";":1, "[":1, "]":1,"{":1, "}":1, "@":1, "|":1, "<":1, "_":1,
            "0":1, "1":1, "2":1, "3":1, "4":1, "5":1, "6":1, "7":1, "8":1, "9":1}

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
            totalFreq = 0
            intervalLength = (interval[END] - interval[BEGIN])
            #logging.info("Old interval:( "+str(interval[BEGIN])+","+str(interval[END])+")")
            for frequency in possibleChars.values():
                totalFreq += frequency

            if self.hasCharacter(character):
                orderedChars = sorted(possibleChars.keys())
                beginning = interval[BEGIN]

                for currentChar in orderedChars:
                    charProb = possibleChars[currentChar] / float(totalFreq)
                    if (character == currentChar):
                        end = beginning + intervalLength*charProb
                        #logging.info("New interval FOUND:("+str(beginning)+","+str(end)+")")
                        return (beginning, end)
                    else:
                        beginning += intervalLength * charProb
            else:
                logging.exception("NO CHARACTER "+str(character)+" at " + CTX_NAME)
                raise interval

        except ZeroDivisionError:
            logging.exception("Divided by zero at context: " + CTX_NAME + "." + str(e))
            return interval


    def compress(self, character, contextList, interval):
        possibleChars = self.getCharacterListWithExclusionPrinciple(contextList)
        newInterval = self.calculateInterval(character, possibleChars, interval)
        return (True, newInterval)
