import Context.py

class Model:

    def __init__(self, number):
        self.number = number
        self.contexts = {}

    def compress(self, text, char_index):
        #Receives a text and an index that indicates
        #the character which is currently being compressed.
        if (index >= self.number):
            #In this case, the model can take the amount of characters
            #indicated by self.number as context

            return True
        #This context could not compress this text because    
        return False
