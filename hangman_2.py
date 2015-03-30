import random 
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.    
    '''
                        
    printedWord = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            printedWord += letter + ' '
        else:
            printedWord += '_ ' 
        return printedWord
                        
                        
                        
                        
                        #guessedWord = '-' * len(secretWord)
                        #if letterGuess in secretWord:
                        #    secretWord[letterGuess] = guessedWord[letterGuess]
                        #    return guessedWord

def loadWord():

    ''' Populate each list with at least 10 different items. Create a variable called secretWord that is assigned a random word from one of the lists. 
    return a tuple in the following format: (secretWord, list the secretWord is from) 
    Hint: You will need to randomly choose one of the lists, and THEN choose a random word from that list.
    '''

    persons = [ 'bridget', 'hannah', 'kane', 'anthony', 'andrew', 'ellen', 'alex', 'amelia', 'chris', 'teri']
    places = ['california', 'florida', 'canada', 'england', 'rome', 'france', 'texas', 'greece', 'vermont', 'serbia']
    things = ['cat', 'iphone', 'computer', 'ipad', 'ipod' ,'steam', 'glitter', 'dragon', 'ring', 'crennelations']
    listOfLists = [persons, places, things]
    randomListChoice = random.choice(listOfLists)
    secretWord = random.choice(randomListChoice)
    if randomListChoice == persons:
        hint = 'person'
    elif randomListChoice == places:
        hint = 'place'
    else:
        hint = 'thing'
    wordAndHintTuple = (secretWord, hint)
                    #if hint == 'person' or hint == 'place' or hint == 'thing':
                    #    loaded == True
    return wordAndHintTuple
                    
def getAvailableLetters(lettersGuessed):

    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise       
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lettersAvailable = alphabet
    for letterGuess in lettersGuessed:
        lettersAvailable.remove(letterGuess)
    return lettersAvailable
                
def isWordGuessed(secretWord, lettersGuessed):
    
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True


def hangman():

    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many 
    letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess 
    about whether their guess appears in the computers word.
    * After each round, you should also display to the user the 
    partially guessed word so far, as well as letters that the 
    user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    #declare all necessary variables
    loaded = loadWord()
    secretWord = loaded[0]
    hint = loaded[1]
    print "Secret word has been loaded..."
    wrongGuesses = 0
    lettersGuessed = []
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    hangmanPics = ['''
+---+
| |
|
|
|
|
=========''', '''
+---+
| |
O 
|
|
|
=========''', '''
+---+
| |
O |
| |
|
|
=========''', '''
+---+
| |
O |
/| |
|
|
=========''', '''
+---+
| |
O |
/|\ |
|
|
=========''', '''
+---+
| |
O |
/|\ |
/ |
|
=========''', '''
+---+
| |
O |
/|\ |
/ \ |
|
=========''']


   
    while wrongGuesses < 6:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            return "You Win!"
        else:
            
            print getAvailableLetters(lettersGuessed)
            letterGuess = raw_input('Please pick a letter:    ')
            letterGuess = letterGuess.lower()
            if len(letterGuess) > 1 or letterGuess not in alphabet or letterGuess not in lettersAvailable:
                letterGuess = raw_input('Please pick an UNUSED LETTER:     ')
            if isLetterInWord == True:
                print 'Good job!'
            if isLetterInWord == False:
                print 'Incorrect'
                wrongGuesses += 1
                print hangmanPics[wrongGuesses + 1]
            print getGuessedWord
            
            #show user available letters print getAvailableLetters(lettersGuessed)
            #get user guess using raw input
            #set guess = guess.lower()
            #make sure guess is valid.  Only 1 character long, must be a letter, and hasnt been used yet. If any of these are true, get user guess again until they are all false
            #check to see if the guess is correct or not.  Is it in the secret Word?
            # If yes, print good job. If no, print incorrect and add 1 to wrong guesses
            #print getGuessedWord(secretWord, lettersGuessed)
            #print appropriate hangman picture (tie index to value of wrongGuesses)