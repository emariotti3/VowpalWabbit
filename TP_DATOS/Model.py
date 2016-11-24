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
            currContext = text[charIndex] if (self.number == 0) else text[charIndex-self.number:charIndex]

            if (currContext in self.contexts):
                return self.contexts[currContext].compress(character, previousContexts, interval)
            elif (currContext != ""):
                #This context does not exist in this model, so we add it.
                self.__add(Context(currContext,character))

        #This context could not compress this text because
        #it does not contain the desired context.
        return (False, interval)

    def __setContext(self, otherContext):
        self.context = otherContext

    def copy(self):
        other = Model(self.number)
        other.__setContext(self.contexts.copy())
        return other
