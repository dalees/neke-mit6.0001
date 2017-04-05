# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"
letters_guessed = []  


PICS = {
    0: "/---\n" +
       "|  |\n" +
       "|  o\n" +
       "| -+-\n" +
       "|  |\n" +
       "| / \\\n" +
       "|\n" +
       "\______\n",
    1: "/---\n" +
       "|  |\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "\______\n",
    2: "/---\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "\______\n",
    3: "/\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "\______\n",
    4: "/\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "\______\n",
    5: "\n" +
       "\n" +
       "\n" +
       "\n" +
       "\n" +
       "\n" +
       "\n" +
       " ______\n",
    6: "\n" +
       "\n" +
       "\n" +
       "\n" +
       "\n" +
       "\n" +
       "\n" +
       "\n",       
}


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    count = 0
    for letter in secret_word:
        if letter in secret_word and letter in letters_guessed:
            count += 1
            if count == len(secret_word):
                return True
        else:
            return False
            break
        

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    sentence = ''
    for letter in secret_word:
        if letter in secret_word and letter in letters_guessed:
            sentence = (sentence + letter)
        else:
            sentence = (sentence + '_ ')
    return (sentence)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = string.ascii_lowercase
    for letter in letters_guessed:
        if letter in letters_guessed and alphabet:
            alphabet = alphabet.replace(letter, "")
    return (alphabet)
    

def hangman(secret_word,):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_left = 6
    warnings_left = 3
    count = len(secret_word)
    alphabet = string.ascii_lowercase
    word = 'guesses'

    you_won = False
    page_break = '---------------'
    input_message = 'What letter would you like to guess?\n'
    letters_not_guessed = 'The letters you have not yet guessed are:'
    #number_guesses_left_message = 'You have {} {} left'.format(guesses_left, word)
    warning = 'Oh no! You haven\'t entered a letter (you just need one!). Try again. But be careful... You only get 3 warnings).'
    warning_already_guessed = 'Oh no! You have already guessed that! Be careful, you only get 3 warnings. Try another letter:\n'
    correct_letter = '\nBravo! You guessed correctly. Your word so far is:\n'
    congrats = '\n!!!!!!!!!!!!!!!!!!\nCongratulations! You guessed the whole word!'
    WRONG_GUESS = '\nUh-oh! That letter is not in the secret word. Your word so far is:'
    out_of_guesses = '\nYou ran out of guesses. Better luck next time! The mystery word was:'
    game_over = 'That was your last warning! Game over. Your word was:'


    print ('\nLet\'s play Hangman!\n')
    print ('The Rules:')
    print ('You have to try and figure out what the mystery word is.')
    print ('You get only one guess per round, and your guess must be a single letter (no numbers or characters).')
    print ('\nLet\'s start!\n')

    print ('The word you are trying to guess has {} letters in it'.format(count))

    while guesses_left != 0 and warnings_left != 0 and not you_won:
        # Get input using message - guess = input(message)
        if guesses_left == 1:
            word = 'guess'
        else:
            word = 'guesses'    
        
        print (page_break)
        print ('You have {} {} left'.format(guesses_left, word))
        print (letters_not_guessed)
        print (get_available_letters(letters_guessed))
        print ('\n')
        guess = input(input_message)
        guess = guess.lower()
        
        if not guess in alphabet or len(guess) != 1:
            warnings_left -= 1
            if warnings_left > 0:
                print (page_break)
                print (warning)
                continue
        if guess in letters_guessed and warnings_left != 0:
            print (warning_already_guessed)
            warnings_left -= 1
                  
        # If the input is bad (warning bad) then decrement warnings and change message appropriately
    
        if guess in alphabet and len(guess) == 1 and not guess in letters_guessed:
            letters_guessed.append(guess)
            
            if guess in secret_word:
                print (correct_letter)
                print (get_guessed_word(secret_word, letters_guessed))
                print ('\n')
                
            else:
                print (WRONG_GUESS)
                print (get_guessed_word(secret_word, letters_guessed))
                print ('\n')                
                print (PICS[guesses_left])
                guesses_left -= 1
                
    if guesses_left == 0:
        print(out_of_guesses, secret_word)
        print(PICS[guesses_left])
        
    elif warnings_left == 0:
        print(PICS[guesses_left])
        print (game_over, secret_word)
        
    elif you_won == True:
        print (congrats)



    # IF the input is sensible
    #   guess add to list of letters guessed
    #   if the input is in the word
    #       do some stuff and set message appropriately
    #   else (input not in the word)
    #       decrement guesses and set message appropriately message = MESSAGE_WRONG_GUESS
    # Print a hangman
# check if num_guesses == 0
#   say you ran outa guesses
# else check if warnings == 0
                
#   say you ran outa warnings
# else (you won)
#   Say you won!


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
   pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
secret_word = choose_word(wordlist)    
hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
