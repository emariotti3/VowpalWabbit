import logging
from Context import Context

class Model(object):

    def __init__(self, number):
        self.number = number
        self.contexts = {}
        self.toAdd = []

    def __add(self, newContext):
        self.toAdd.append(newContext)

    def __refreshModel(self):
        for i in xrange(0,len(self.toAdd)):
            currContext = self.toAdd.pop(i)
            if (not currContext in self.contexts):
                self.contexts[currContext.name()] = currContext
        self.toAdd = []

    def compress(self, text, charIndex, previousContexts, interval):
        self.__refreshModel()
        if (charIndex >= self.number):
            #In this case, the model can take the amount of characters
            #indicated by self.number as context
            character = text[charIndex]
            #logging.info( "MODEL #"+str(self.number))
            currContext = text[charIndex] if (self.number == 0) else text[charIndex-self.number:charIndex]
            #logging.info( "compressing (" +str(currContext)+ ")" + str(character))
            #logging.info( "available contexts:" +str(self.contexts.keys()))

            if (currContext in self.contexts):
                return self.contexts[currContext].compress(character, previousContexts, interval)
            elif (currContext != ""):
                #This context does not exist in this model, so we add it.
                self.__add(Context(currContext,character))
                #logging.info( "Added context:" + currContext + " to model "+str(self.number))

        #This context could not compress this text because
        #it does not contain the desired context.
        return (False, interval)
