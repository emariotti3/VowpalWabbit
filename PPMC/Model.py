import Context.py

class Model:

    def __init__(self, number):
        self.number = number
        self.contexts = {}

    def compress(self, text, charIndex, previousContexts, interval):
        #Receives a text and an index that indicates
        #the character which is currently being compressed.
        #Receives a list with all the previousContexts that have
        #tried to compress this character and the compression interval.

        if (index >= self.number):
            #In this case, the model can take the amount of characters
            #indicated by self.number as context
            character = text[charIndex]
            currContext = text[charIndex-self.number:charIndex-1]
            if (currContext in self.contexts.keys()):
                #Tell the context to try and compress the desired character.
                newInterval = self.contexts[currContext].tryCompress(character,previousContexts,interval)
                return (newInterval != interval):
            else:
                #This context does not exist in this model, so we add it.
                self.contexts[currContext] = Context(currContext,character)
        #This context could not compress this text because
        #it does not contain the desired context.
        return False
