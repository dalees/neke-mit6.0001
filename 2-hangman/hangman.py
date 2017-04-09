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

PICS1 = {

    -1:"/-----\n" +
       "|   |\n" +
       "|   😣\n" +
       "| --+--\n" +
       "|   |\n" +
       "|  / \\\n" +
       "|\n" +
       "\______\n",
       
     0:"/-----\n" +
       "|   |\n" +
       "|   😣\n" +
       "| --+--\n" +
       "|   |\n" +
       "|  / \\\n" +
       "|\n" +
       "\______\n",  
    1: "/-----\n" +
       "|    |\n" +
       "|   😭\n" +
       "|  --+--\n" +
       "|    |\n" +
       "|\n" +
       "|\n" +
       "\______\n",
    
    2: "/-----\n" +
       "|    |\n" +
       "|   😧\n" +
       "|  --+--\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "\________\n",
       
    3: "/-----\n" +
       "|    |\n" +
       "|   😠\n" +
       "|    +\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "\________\n",        
    4: "/-----\n" +
       "|    |\n" +
       "|   😒\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "\________\n",
    5: "/-----\n" +
       "|    |\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "\________\n",
    6: "/-----\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "\________\n",
    7: "/\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "\________\n",
    8: "\n" +
       "\n" +
       "\n" +
       "\n" +
       "\n" +
       "\n" +
       "\n" +
       " ________\n",
    9: "\n" +
       "\n" +
       "\n" +
       "\n" +
       "\n" +
       "\n" +
       "\n" +
       "\n",       
}

PICS2 = {
    -1:"/-----\n" +
       "|    |\n" +
       "|    😣\n" +
       "|  --+--\n" +
       "|    |\n" +
       "|   / \\\n" +
       "|\n" +
       "\________\n",
    0: "/-----\n" +
       "|    |\n" +
       "|    😣\n" +
       "|  --+--\n" +
       "|    |\n" +
       "|   / \\\n" +
       "|\n" +
       "\________\n",
    1: "/-----\n" +
       "|    |\n" +
       "|   😧\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "\________\n",
    2: "/-----\n" +
       "|    |\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "\________\n",
    3: "/-----\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "\________\n",
    4: "/\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "\________\n",
    5: "\n" +
       "\n" +
       "\n" +
       "\n" +
       "\n" +
       "\n" +
       "\n" +
       " ________\n",
    6: "\n" +
       "\n" +
       "\n" +
       "\n" +
       "\n" +
       "\n" +
       "\n" +
       "\n",       
}

PICS3 = {
    -1:"/-----\n" +
       "|    |\n" +
       "|    😣\n" +
       "|  --+--\n" +
       "|    |\n" +
       "|   / \\\n" +
       "|\n" +
       "\________\n",
    0: "/-----\n" +
       "|    |\n" +
       "|    😣\n" +
       "|  --+--\n" +
       "|    |\n" +
       "|   / \\\n" +
       "|\n" +
       "\________\n",
    1: "/-----\n" +
       "|    |\n" +
       "|   😧\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "\________\n",
    2: "/-----\n" +
       "|    |\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "\________\n",
    3: "/-----\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "\________\n",
    4: "/\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "|\n" +
       "\________\n",
    5: "\n" +
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
    inFile.close()
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


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
        

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    sentence = ''
    for letter in secret_word:
        if letter in letters_guessed:
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
    letters_guessed = []  
    word = 'guesses'
    warning_word = 'warnings'
    vowels = 'aeiou'

    #variables for different messages
    you_won = False #the you_won variable points to the is_word_guessed function when it needs to check if your answer matches
    PAGE_BREAK = '---------------'
    input_message = 'What letter would you like to guess?\n'
    letters_not_guessed = 'The letters you have not yet guessed are:'
    warning = 'Oh no! You haven\'t entered a letter (you just need one!). You have: {} {} left.'
    warning_already_guessed = 'Oh no! You have already guessed that! Be careful, you only have {} {} left.\n'
    CORRECT_LETTER = '\nBravo! You guessed correctly. Your word so far is:\n'
    CONGRATS = '!!!!!!!!!!!!!!!!!!\nCongratulations! You guessed the whole word!n!!!!!!!!!!!!!!!'
    WRONG_GUESS = '\nUh-oh! That letter is not in the secret word. Your word so far is:'
    WRONG_GUESS_VOWEL = '\nUh-oh! That letter is not in the secret word. You lose 2 guesses because it was a vowel. Your word so far is:'    
    OUT_OF_GUESSES = '\nYou ran out of guesses. Better luck next time! The mystery word was:'
    OUT_OF_WARNINGS = 'That was your last warning! Now you lose a guess.'

    #introduction and rules to print on startup
    print ('\nLet\'s play Hangman!\n')
    print ('The Rules:')
    print ('You have to try and figure out what the mystery word is.')
    print ('You get only one guess per round, and your guess must be a single letter (no numbers or characters).')
    print ('You lose 1 guess for an incorrect consonant and 2 guesses for an incorrect vowel')    
    print ('\nLet\'s start!\n')
    print ('The word you are trying to guess has {} letters in it'.format(count))

    #while you have guesses left and you haven't won
    while guesses_left > 0 and not you_won:
        if guesses_left == 1:
            word = 'guess' #to correct grammar
        else:
            word = 'guesses'    
        
        #tells you how many guesses you have left, what letters left, and asks you to input a letter
        print (PAGE_BREAK)
        print ('You have {} {} left'.format(guesses_left, word))
        print (letters_not_guessed)
        print (get_available_letters(letters_guessed))
        print ('\n')
        guess = input(input_message)
        guess = guess.lower()

        # If the input is not appropriate (not a single letter or not in alphabet), then decrement warnings and print warning message
        if not guess in alphabet or len(guess) != 1 or guess in letters_guessed: # if letter isn't in alphabet or it's more than 1 letter

            if guess in letters_guessed and warnings_left > 0: # if you've already guessed it
                    warnings_left -= 1
                    if warnings_left == 1:
                        warning_word = 'warning'
                    print (warning_already_guessed.format(warnings_left, warning_word))
            
            elif warnings_left > 0: # 
                warnings_left -= 1
                print (PAGE_BREAK)
                print (warning.format(warnings_left, warning_word))
                continue
            
            #if you run out of warnings you lose a guess   
            elif warnings_left == 0:
                guesses_left -= 1
                warnings_left = 3
                print ()
                print(PICS[guesses_left])
                print (OUT_OF_WARNINGS)
        
        #if the input letter meets the requirements (in the alphabet, not already guessed and only 1 letter)
        if guess in alphabet and len(guess) == 1 and not guess in letters_guessed:
            letters_guessed.append(guess)
            
            if guess in secret_word:
                print (CORRECT_LETTER)
                print (get_guessed_word(secret_word, letters_guessed))
                print ('\n')
                you_won = is_word_guessed(secret_word, letters_guessed)
        
            #if the guess is a vowel and it's wrong, lose 2 guesses
            elif guess in vowels:
                guesses_left -=2
                print (WRONG_GUESS_VOWEL)
                print (get_guessed_word(secret_word, letters_guessed))
                print ('\n')
                print (PICS[guesses_left])
                
            #print wrong guess and decrease number of guesses left by 1            
            else:
                guesses_left -= 1
                print (WRONG_GUESS)
                print (get_guessed_word(secret_word, letters_guessed))
                print ('\n')                
                print (PICS[guesses_left])
                        
    #you've run out of guesses, game over
    if not guesses_left > 0:
        print(OUT_OF_GUESSES, secret_word)

    #you won, you guessed all the letters  
    elif you_won:
        print (CONGRATS)
        print ('\nYour score is:', guesses_left * len(letters_guessed))


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
    my_word = my_word.replace(" ", "") #remove spaces in my_word
    if len(my_word) == len(other_word): # if the length of my_word and other_word are the same
        for my_letter, other_letter in zip(my_word, other_word): # if the letters of both words match, ignoring the _ letters
            if my_letter != other_letter and my_letter != '_':
                return False
        return True
    else:
        return False

def get_best_letter(words_list, ignore_letters):
    # Version1: just find the most common letter
    letter_counts = {}
    for word in words_list:
      for letter in word:
        if letter in ignore_letters:
          continue
        if letter not in letter_counts:
          letter_counts[letter] = 0
        letter_counts[letter] += 1

    letter_best = None
    letter_best_count = 0
    for letter, count in letter_counts.items():
      if count > letter_best_count:
        letter_best_count = count
        letter_best = letter

    return letter_best

def show_possible_matches(my_word, letters_guessed):
    """
    my_word: string with _ characters, current guess of secret word
    letters_guessed: string of characters already guessed
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    """ 
    
    def check_possible_match(my_word, other_word, letters_guessed):
        """
        my_word: string with _ characters, current guess of secret word
        other_word: string to check against for matchiness
        letters_guessed: string of characters already guessed
        returns: true if the match fits. The match can't have any unguessed letters
                 that are in the same position as _ characters
        
        """
        
        if not match_with_gaps(my_word, other_word):
            return False
        
        for my_letter, other_letter in zip(my_word, other_word): # for each letter in word check against corresponding letter in other word
            if my_letter == '_' and other_letter in letters_guessed: # if my_word has an _ and that letter in other_word has already been guessed, return False
                return False    
        return True
    
    my_word = my_word.replace(" ", "")
    matched_words = []
    for word in wordlist:
        if check_possible_match(my_word, word, letters_guessed): # makes a list of words that are possible matches 
            matched_words.append(word)
    
    if len(matched_words) == 0:
        print ('There are no matches.')
        return
    
    if len(matched_words) > 20:
        print (", ".join(matched_words[0:20]), "....... and MANY MORE! (", len(matched_words), ")")
    else:
        print (', '.join(matched_words))

    # Find the letter that will reveal the most about the target word
    best_letter = get_best_letter(matched_words, letters_guessed)
    print ('The most common unguessed letter of the possible words is ', best_letter)


def select_word_length(word, lengths,):
    """
    takes list of word and list of lengths
    returns only words the right length
    """
    right_length_words = []
    
    for word in wordlist:
        if not len(word) in lengths:
            pass
        else:
            right_length_words.append(word)
            
    return right_length_words
            

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
    guesses_left = 6
    warnings_left = 3
    count = len(secret_word)
    alphabet = string.ascii_lowercase
    letters_guessed = []  
    word = 'guesses'
    warning_word = 'warnings'
    vowels = 'aeiou'
    hint_count = 0
    hint_word = 'hints'

    #variables for different messages
    you_won = False #the you_won variable points to the is_word_guessed function when it needs to check if your answer matches
    PAGE_BREAK = '---------------'
    input_message = 'What letter would you like to guess?\n'
    letters_not_guessed = 'The letters you have not yet guessed are:'
    warning = 'Oh no! You haven\'t entered a letter (you just need one!). You have: {} {} left.'
    warning_already_guessed = 'Oh no! You have already guessed that! You have {} {} left.\n'
    CORRECT_LETTER = '\nBravo! You guessed correctly. Your word so far is:\n'
    CONGRATS = '!!!!!!!!!!!!!!!!!!\nCongratulations! You guessed the whole word\n!!!!!!!!!!!!!!!!!!'
    WRONG_GUESS = '\nUh-oh! That letter is not in the secret word. Your word so far is:'
    WRONG_GUESS_VOWEL = '\nUh-oh! That letter is not in the secret word. You lose 2 guesses because it was a vowel. Your word so far is:'    
    OUT_OF_GUESSES = '\nYou ran out of guesses. Better luck next time! The mystery word was:'
    OUT_OF_WARNINGS = 'That was your last warning! Now you lose a guess.'
    HINT = 'You want a hint!? How tragic that you cannot figure it out for yourself. Very well, the possible matches are:'
    NO_HINTS = '...and you didn\'t use any hints! Brilliant!'
    HINT_COUNTER = '...but you used {} {}. Cheater. We should probably change that score to {}...'
    
    #introduction and rules to print on startup
    print ('\nLet\'s play Hangman!\n')
    
    #choose difficulty level. adjusts the pictures printed and word length based on difficulty
    difficulty = input('\nChoose your difficulty level. Enter 1, 2 or 3 (for Easy, Normal or Extra Hard):\n')
    if difficulty == '1':
        PICS = PICS1
        guesses_left = 9
    elif difficulty == '2':
        PICS = PICS2
    elif difficulty == '3':
        PICS = PICS3
        guesses_left = 5
        secret_word = choose_word(select_word_length(wordlist, [5,6,7]))
                        
    print ('\nThe Rules:')
    print ('You have to try and figure out what the mystery word is.')
    print ('You get only one guess per round, and your guess must be a single letter (no numbers or characters).')
    print ('If you can\'t figure it out and need a hint, enter the * symbol instead of a letter.')    
    print ('You lose 1 guess for an incorrect consonant and 2 guesses for an incorrect vowel')    
    print ('\nLet\'s start!\n')
    print ('The word you are trying to guess has {} letters in it'.format(count))

    #while you have guesses left and you haven't won
    while guesses_left > 0 and not you_won:
        if guesses_left == 1:
            word = 'guess' #to correct grammar
        else:
            word = 'guesses'    
        
        #tells you how many guesses you have left, what letters left, and asks you to input a letter
        print (PAGE_BREAK)
        print ('You have {} {} left'.format(guesses_left, word))
        print (letters_not_guessed)
        print (get_available_letters(letters_guessed))
        print ('\n')
        guess = input(input_message)
        guess = guess.lower()
        
        """
        if guess == "debug":
            print(secret_word, letters_guessed)
        """
        # If the input is not appropriate (not a single letter or not in alphabet), then decrement warnings and print warning message
        if not guess in alphabet or len(guess) != 1 or guess in letters_guessed: # if letter isn't in alphabet or it's more than 1 letter
            
            if guess == '*':
                print (PAGE_BREAK)
                print (HINT, '\n')
                show_possible_matches(get_guessed_word(secret_word, letters_guessed), letters_guessed)
                hint_count += 1
                print ('\n')
                print ('Your word so far is:', get_guessed_word(secret_word, letters_guessed))
                continue            
            
            if guess in letters_guessed and warnings_left > 0: # if you've already guessed it
                    warnings_left -= 1
                    if warnings_left == 1:
                        warning_word = 'warning'
                    print (warning_already_guessed.format(warnings_left, warning_word))
            
            elif warnings_left > 0: # if it's not a single letter
                warnings_left -= 1
                print (PAGE_BREAK)
                print (warning.format(warnings_left, warning_word))
                continue
            
            #if you run out of warnings you lose a guess   
            elif warnings_left == 0:
                guesses_left -= 1
                warnings_left = 3
                print ()
                print(PICS[guesses_left])
                print (OUT_OF_WARNINGS)
        
        #if the input letter meets the requirements (in the alphabet, not already guessed and only 1 letter)
        if guess in alphabet and len(guess) == 1 and not guess in letters_guessed:
            letters_guessed.append(guess)
            
            if guess in secret_word:
                print (CORRECT_LETTER)
                print (get_guessed_word(secret_word, letters_guessed))
                print ('\n')
                you_won = is_word_guessed(secret_word, letters_guessed)
        
            #if the guess is a vowel and it's wrong, lose 2 guesses
            elif guess in vowels:
                guesses_left -=2
                print (WRONG_GUESS_VOWEL)
                print (get_guessed_word(secret_word, letters_guessed))
                print ('\n')
                print (PICS[guesses_left])
                
            #print wrong guess and decrease number of guesses left by 1            
            else:
                guesses_left -= 1
                print (WRONG_GUESS)
                print (get_guessed_word(secret_word, letters_guessed))
                print ('\n')                
                print (PICS[guesses_left])
                        
    #you've run out of guesses, game over
    if not guesses_left > 0:
        print(OUT_OF_GUESSES, secret_word)

    #you won, you guessed all the letters  
    elif you_won:
        print (CONGRATS)
        score = guesses_left * len(letters_guessed)
        if difficulty == '3':
            score = score + 10
        elif difficulty == '1':
            score = score - 15
        print ('\nYour score is:', score) # print your score taking into consideration difficulty level
        
        # your score taking into consideration number of hints used      
        if hint_count == 0:
            print (NO_HINTS)
        else:
            new_count = int(score / (hint_count * 2))
            if hint_count == 1:
                hint_word = 'hint'
            if score >= 2:
                print (HINT_COUNTER.format(hint_count, hint_word, new_count))
            elif score <= 1:
                score = score - 1
                print (HINT_COUNTER.format(hint_count, hint_word, score))




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    
    wordlist = load_words()
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.



#print (match_with_gaps('t_u_k', 'truck'))


###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
