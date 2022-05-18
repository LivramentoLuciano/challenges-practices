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
import os

WORDLIST_FILENAME = "words.txt"
INITIAL_GUESSES = 6
INITIAL_WARNINGS = 3
VOWELS = ['a', 'e', 'i', 'o', 'u']
# caracter para letras aun no adivinadas
BLANK = '_ '

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


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
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
    # con las letras que se fueron ingresando, capturo las correctas
    # y chequeo si ya forman la palabra completa
    guessed_word = get_guessed_word(secret_word, letters_guessed)
    return secret_word == guessed_word


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # Nota: importante que me di cuenta haciendolo, que intuitivamente lo hubiera hecho al reves
    # recorriendo las letters_guessed y fijandome si estaban en la secret_word, lo cual hubiera
    # sido un quilombaso, porque tenes que guardarte el index en q aparece y si esta dos o mas veces
    # te re complica. Por tanto, esta forma resuelve todo de manera super sencilla. Recordarlo!

    # recorro la secret word y chequeo c/ letra 
    # si fue adivinada, la agrego
    # sino, espacio en blanco ('_ ')
    guessed_word_list = [
        s_letter if s_letter in letters_guessed else BLANK 
        for s_letter in secret_word
    ]

    guessed_word = ''.join(guessed_word_list)
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # full english letters (lowercase)
    full_letters = string.ascii_lowercase
    
    # de estas, elimino las que ya fueron 'guessed'
    available_letters_list = [ 
      letter 
      for letter in full_letters 
      if letter not in letters_guessed
    ] 
    available_letters = ''.join(available_letters_list)

    # sin list_comprehension (recordar str inmmutable, se crean copias)
    # available_letters = full_letters
    # for l in letters_guessed:
    #   available_letters = available_letters.replace(l,'')

    return available_letters


def get_score(secret_word, guesses_left):
  unique_letters_secret = list(set(secret_word))
  num_unique_letters_secret = len(unique_letters_secret)
  
  score = guesses_left * num_unique_letters_secret
  return score

    
def hangman(secret_word):
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
    # Mensaje de Bienvenida del Juego
    print(f'''🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴
    Bienvenido al Ahorcado!
    Estoy pensando en una palabra con... {len(secret_word)} letras.
    --------------
    ''')

    # condiciones iniciales
    warnings_left = INITIAL_WARNINGS
    guesses_left = INITIAL_GUESSES
    letters_guessed = []
    guessed_word = get_guessed_word(secret_word, letters_guessed)

    # Comienza loop-infinito del Juego
    while True:
      available_letters = get_available_letters(letters_guessed)

      if guesses_left == 0: 
        you_lost(secret_word)      
      
      print(f'Te quedan {guesses_left} intentos para adivinar letras.')
      print(f'Letras disponibles: {available_letters}')
      
      # ingreso letra (guess)
      guess = input('Por favor, haz un intento por adivinar una letra: ')
      
      # Valido que sea alfabetica y no haya sido ya ingresada
      # De ser invalido, imprimo advertencia y vuelvo a pedir letra o quito intento de guess
      if not guess.isalpha() or  guess in letters_guessed:
        warnings_left -= 1
        if warnings_left > 0: 
          print(f'Oops! Has ingresado una letra inválida o repetida. Te quedan {warnings_left} advertencias.')          
        else: 
          print(f'Oops! Has ingresado una letra inválida o repetida y gastaste tus advertencias. Se te descontará un intento.')
          guesses_left -= 1
          # warnings_left = INITIAL_WARNINGS

        print(f'{guessed_word}')
        print('----------------------')
        continue

      # caracter es valido, lo agrego a mi lista de 'letters_guessed'
      # durante el programa utilizamos todo en minuscula, para simplificar
      guess = guess.lower()
      letters_guessed.append(guess)      

      # chequeo si se encuentra en la secret_word e imprimo resultado
      if guess in secret_word:
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        if is_word_guessed(secret_word, letters_guessed): 
          score = get_score(secret_word, guesses_left)
          you_win(score, secret_word)
        else: 
          print(f'Bien hecho, encontraste una nueva letra: {guessed_word}')
      else:
        guesses_left -= 2 if guess in VOWELS else 1
        print(f'Oops! La letra no está en mi palabra: {guessed_word}')

      print('----------------------')


def you_win(score, word):
  print('\n🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳')
  print(f'Felicitaciones! Has completado el juego, con un total de {score} puntos')
  print(f'Adivinaste la palabra: {word.upper()}')
  exit_game()

def you_lost(word):
  print('🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡')
  print(f'Te has quedado sin intentos. La palabra correcta era {word.upper()}')
  exit_game()  

def exit_game():  
  print('Muchas gracias por jugar. Hasta pronto! 👋')

  # pregunto si desea volver a jugar
  keep_playing = input('\n Presiona "Q" para salir, cualquier otra tecla para volver a jugar.')
  # limpio pantalla
  os.system('cls')
  if keep_playing != 'Q' and keep_playing != 'q': main()
  else: exit()


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # remuevo espacios en los caracteres BLANK ('_ ') de my_word
    my_word = my_word.replace(' ', '')   

    # si tienen distinto tamaño ya la descarto
    if len(my_word) != len(other_word): return False

    # Ahora, chequeo si my_word puede llegar a ser la other_word
    # contrasto solo los casos que me dan False y listo
    for i in range(len(my_word)):
      my_letter = my_word[i]
      other_letter = other_word[i]

      # comparo con el guión solo porque removi los espacios en bco
      if my_letter == BLANK.strip():
        # chequeo que no debiera ir una letra ya adivinada aqui en realidad
        if other_letter in my_word:
          return False

      elif my_letter != other_letter:          
          return False

    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches = [
      word
      for word in wordlist
      if match_with_gaps(my_word, word)
    ]

    if possible_matches: print(f'{possible_matches}')
    else: print('No se han encontrado coincidencias posibles')


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
    # Mensaje de Bienvenida del Juego
    print(f'''🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴🕴
    Bienvenido al Ahorcado!
    Estoy pensando en una palabra con... {len(secret_word)} letras.
    --------------
    ''')

    # condiciones iniciales
    warnings_left = INITIAL_WARNINGS
    guesses_left = INITIAL_GUESSES
    letters_guessed = []
    guessed_word = get_guessed_word(secret_word, letters_guessed)

    # Comienza loop-infinito del Juego
    while True:
      available_letters = get_available_letters(letters_guessed)
      
      if guesses_left == 0:
        you_lost(secret_word)      
      
      print(f'Te quedan {guesses_left} intentos para adivinar letras.')
      print(f'Letras disponibles: {available_letters}')
      
      # ingreso letra (guess)
      guess = input('Por favor, haz un intento por adivinar una letra: ')

      # antes de proseguir con el hangman normal, chequeo si pidio HINT
      if guess == '*':
        print('Has solicitado una pista, la palabra se encuentra entre las siguientes:')
        show_possible_matches(guessed_word)
        print('----------------------')
        continue
      
      # Valido que sea alfabetica y no haya sido ya ingresada
      # De ser invalido, imprimo advertencia y vuelvo a pedir letra o quito intento de guess
      if not guess.isalpha() or  guess in letters_guessed:
        warnings_left -= 1
        if warnings_left > 0: 
          print(f'Oops! Has ingresado una letra inválida o repetida. Te quedan {warnings_left} advertencias.')          
        else: 
          print(f'Oops! Has ingresado una letra inválida o repetida y gastaste tus advertencias. Se te descontará un intento.')
          guesses_left -= 1
          # warnings_left = INITIAL_WARNINGS
        print(f'{guessed_word}')
        print('----------------------')
        continue

      # caracter es valido, lo agrego a mi lista de 'letters_guessed'
      # durante el programa utilizamos todo en minuscula, para simplificar
      guess = guess.lower()
      letters_guessed.append(guess)      

      # chequeo si se encuentra en la secret_word e imprimo resultado
      if guess in secret_word:
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        if is_word_guessed(secret_word, letters_guessed): 
          score = get_score(secret_word, guesses_left)
          you_win(score, secret_word)
        else: 
          print(f'Bien hecho, encontraste una nueva letra: {guessed_word}')
      else:
        guesses_left -= 2 if guess in VOWELS else 1
        print(f'Oops! La letra no está en mi palabra: {guessed_word}')

      print('----------------------')

def main():
  # secret_word = choose_word(wordlist)
  # hangman(secret_word)
    
  secret_word = choose_word(wordlist)
  hangman_with_hints(secret_word)  

if __name__ == "__main__":   
  main() 

