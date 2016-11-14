from Model import Model
from BaseContext import BaseContext

class BaseModel(Model):

    def __init__(self):
        super(BaseModel,self).__init__(-1)
        self.context = BaseContext()

    def compress(self, text, charIndex, previousContexts, interval):
        character = text[charIndex]
        print "MODEL #-1\n"
        return self.context.compress(character, previousContexts, interval)
