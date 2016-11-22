import logging
from Model import Model
from BaseContext import BaseContext

class BaseModel(Model):

    def __init__(self):
        super(BaseModel,self).__init__(-1)
        self.context = BaseContext()

    def compress(self, text, charIndex, previousContexts, interval):
        character = text[charIndex]
        #logging.info("Compressed character: "+ character + " at MODEL -1")
        return self.context.compress(character, previousContexts, interval)
