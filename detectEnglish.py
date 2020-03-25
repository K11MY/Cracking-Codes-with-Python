# Define letters
UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def loadDictionary():
    #Open dictionary file
    dictionaryFile = open('dictionary.txt')
    #Initialise englishwords dict
    englishWords = {}
    #Loop (read dictionary file and split at each space)
    for word in dictionaryFile.read().split('\n'):
        #Store value of word as None (as there is no value for the key)
        englishWords[word] = None
    #close dictionary
    dictionaryFile.close()
    return englishWords
#Assign english words to dictionary
ENGLISH_WORDS = loadDictionary()

def getEnglishCount(message):
    #change message to upper case
    message = message.upper()
    #remove non letters in the message
    message = removeNonLetters(message)
    #store possible words from message
    possibleWords = message.split()
    #Ensures we don't get the divide by zero error
    if possibleWords == []:
        return 0.0 # No words at all, so return 0.0.

    #Countes  english word matches
    matches = 0
    #Loop through words in possible word
    for word in possibleWords:
        # if the word is in english words add a to matches
        if word in ENGLISH_WORDS:
            matches += 1
    #Return ratio
    return float(matches) / len(possibleWords)

#Remove full stops, commas and etc
def removeNonLetters(message):
    #Initalise list of letters only
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)


def isEnglish(message, wordPercentage=20, letterPercentage=85):
    # By default, 20% of the words must exist in the dictionary file, and
    # 85% of all the characters in the message must be letters or spaces
    # (not punctuation or numbers).
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch