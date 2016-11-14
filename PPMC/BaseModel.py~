import Model.py
import BaseContext.py

class BaseModel(Model):

    def __init__(self):
        super(Model,self).__init__(-1)
        self.context = BaseContext()

    def compress(self, text, charIndex, previousContexts, interval):
        character = text[charIndex]
        return self.context.compress(character, previousContexts, interval)
