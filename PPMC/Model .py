from Context import Context

class Model(object):

    def __init__(self, number):
        self.number = number
        self.contexts = {}

    def compress(self, text, charIndex, previousContexts, interval):
        if (charIndex >= self.number):
            #In this case, the model can take the amount of characters
            #indicated by self.number as context
            character = text[charIndex]
            currContext = text[charIndex-self.number:charIndex-1]

            for contextName, context in self.contexts.items():
                if (contextName == currContext):
                    return context.compress(character, previousContexts, interval)
                else:
                    #This context does not exist in this model, so we add it.
                    self.contexts[currContext] = Context(currContext,character)
        #This context could not compress this text because
        #it does not contain the desired context.
        return (False, interval)
