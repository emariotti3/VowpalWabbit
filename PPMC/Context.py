ESCAPE = "ESC"
INIT_FREQUENCY = 2
PREVIOUS_CONTEXTS_LIST = 0
COMPRESSION_PROBABILITY = 1

class Context:

    def __init__(self, conext_key, character):
        self.key = context_key
        self.seen_chars = {}
        self.total_seen = INIT_FREQUENCY
        self.seen_chars[ESCAPE] = 1
        self.seen_chars[character] = 1
        self.char_to_add = ""

    def is(context_key):
        return (self.key == key)

    def hasCharacter(self, character):
        return character in self.seen_chars.keys()

    def __refreshContext(self):
        
        if (not self.char_to_add):
            return False
        if (self.has_character(self.to_add)):
            self.seen_chars[self.to_add] += 1
        else:
            self.seen_chars[self.to_add] = 1
            self.seen_chars[ESCAPE] += 1
            self.total_seen += 1
        self.total_seen += 1
        self.to_add = ""
        return True

    def add(character):
        #adds a character to be added to context in following compression step
        self.to_add = character

    def compress(self, character, context):
        #Recives a character to be compressed and a tuple context = (previous_contexts, compression_prob),
        #where 'previous_contexts' is a list of all the contexts
        #that have tried to compress this character and 'compression_prob' is the
        #emitted compression probability of said character in the previous context.

        #Returns a tuple that contains (previous_contexts, compression_prob),
        #where 'previous_contexts' is the list of all previous contexts including this one.
        #The value returned for 'compression_prob' will not vary if a previous context
        #had already compressed (compression_prob != 0).
        #The compression_prob will equal 0 if this context cannot compress the desired character
        #and previous contexts could not compress either (compression_prob == 0).
        #If the context is able to compress this character, compression_prob
        #will equal that character's compression probability in this context.

        #This method will also add the character to the list of seen characters,
        #so there is no need to add it manually.
        try:
            self.refresh_context()
            if (context[COMPRESSION_PROBABILITY] != 0):
                return context

            compression_prob = 0
            context_list = context[PREVIOUS_CONTEXTS_LIST]

            if (not self.has_character(character))
                context_list.append(self)
            else:
                totalSeenWithContext = self.total_seen
                for (seen_char in self.seen_chars):
                    previously_seen = False
                    context_list = context[PREVIOUS_CONTEXTS_LIST]
                    while ((not previously_seen) and context_list):
                        current_context = context_list[0]
                        if (context.has_character(seen_char)):
                            totalSeenWithContext -= 1
                            previously_seen = True
                        context_list.pop(0)

                compression_prob = self.seen_chars[character] / totalSeenWithContext

            new_context = (context_list, compression_prob)
            self.add(character)
            return new_context

        catch(Exception):
            return (context_list, 0)
