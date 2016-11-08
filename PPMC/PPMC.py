
stopWords = ["a","about","above","across","after","afterwards", "are","around","as","at","be", "because", "been",
             "for","go", "had","has", "have", "him", "his", "her", "hers", "them", "in", "on","theirs", ".", ",", "-",
             "it", "is", "was", "who", "when", "where", "which", "what", "that", "the", "there", "they", "then", "this",
             "got", "i", "an", "to", "under", "through", "of", "since", "and", "you", "get", "out", "or", "up", "down"]

MAX_CHAR_SIZE = 8
CHAR_PROBABILITY = 2 ** MAX_CHAR_SIZE + 1 #ALL 8 BIT COMBINATIONS + EOF
PPMC_ORDER = 4 #PRESUMABLY THE "BEST" ORDER

def ppmc(text):
    compressed_val = 0

    return compressed_val
