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
    
    def __setBaseContext(self, otherBaseContext):
        self.context = otherBaseContext.copy()
    
    def copy(self):
        other = BaseModel()
        other.__setBaseContext(self.context.copy())
        return other
        