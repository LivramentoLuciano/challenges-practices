# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
WILDCARD = '*'
FINISH_INPUT = "!!"
SUBSTITUTIONS = 1
REPLAYS = 1

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, WILDCARD: 0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...", end=" ")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print(len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    word = word.lower()
    letters_score = [ SCRABBLE_LETTER_VALUES[letter] for letter in word ]
    
    length_score = 7*len(word) - 3*(n-len(word))
    if length_score < 1: length_score = 1
    
    score = sum(letters_score) * length_score
    return score

#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3)) - 1

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    # agrego 1 wildcard
    hand[WILDCARD] = 1
    
    return hand

#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # copio la mano original para no modificarla
    new_hand = hand.copy()
    word = word.lower()
    
    for letter in word:
        l_count = new_hand.get(letter)
        # si la letra usada existía en la mano
        # y no la use mas veces de las que tenia en la mano
        if l_count != None and l_count > 0:
            new_hand[letter] -= 1

    # print(new_hand)
    return new_hand

#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    # metodo interno, chequeo de una palabra (sin wildcard)
    def _is_valid_word(word, hand, word_list):
        # si no existe la palabra, pongo con False
        if word not in word_list: return False

        # si existe, chequeo que haya usado las letras
        # que tenia en la mano y en cantidad correcta

        # transformo la 'word' al mismo formato que 'hand' (dict)
        word_dict = get_frequency_dict(word)

        for l,count in word_dict.items():
            if hand.get(l) == None or hand.get(l) < count:
                return False
        return True        

    word = word.lower()
    # print(f'Palabra original: {word} - Mano original: {hand}')

    # primero chequeo si utilizo 'wildcard'
    if WILDCARD in word:
        # IMPORTANTE: para que _is_valid_word funcione
        # reemplazar en la hand, la WILDCARD por la vocal candidata

        # Armo dict con la wildword / wildhand 
        wild_candidates = {}
        for vowel in VOWELS:
            # hand y word posibles, reemplazando wildcard por la vocal
            # elimino la wildcard de la hand, 
            # en su lugar coloco/sumo 1 a la vocal correspondiente
            v_wildhand = hand.copy()
            del v_wildhand[WILDCARD]
            v_wildhand[vowel] = v_wildhand.get(vowel, 0) + 1

            # palabra candidata, reemplazando wildcard por la vocal
            v_wildword = word.replace(WILDCARD, vowel)

            # agrego a dict de wild_candidates, la word y hand de la vocal correspondiente
            vowel_dict = { 'wildword': v_wildword, 'wildhand': v_wildhand }
            wild_candidates[vowel] = vowel_dict
            
        # si al menos 1 de las candidatas es valida -> True
        valid = any(
            _is_valid_word(candidate['wildword'], candidate['wildhand'], word_list)
            for _,candidate in wild_candidates.items()
        )
        return valid
    else:
        return _is_valid_word(word, hand, word_list)

    
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    handlen = 0
    for _,lcount in hand.items():
        handlen += lcount
        
    # handlen = sum([
    #     lcount
    #     for _,lcount in hand.items()
    # ])
    return handlen

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    hand_score = 0
    handlen = calculate_handlen(hand)
    while handlen > 0:
        print('Mano actual: ', end=' ')
        display_hand(hand)

        # ingresar palabra o "!!" para terminar
        word = input('Ingrese una palabra, o "!!" si desea finalizar: ')
        word = word.lower()

        # si ingreso "!!" finalizar. Mostrar puntaje total.
        if word == FINISH_INPUT:
            print()
            break
        
        # verifico si es valida
        # si es valida, calcular los puntos y sumar al total
        if is_valid_word(word, hand, word_list):
            word_score = get_word_score(word, handlen)
            hand_score += word_score
            print(f'"{word}" suma {word_score} puntos. Total: {hand_score} puntos.')
        else:
            print('La palabra ingresada NO es válida. Por favor, ingresa otra.')
        
        # sea o no valida, consume las letras usadas (actualizo hand)
        hand = update_hand(hand, word)

        # volver a empezar con las letras restantes
        handlen = calculate_handlen(hand)
        # print()
        print('---------------------------------')
    
    # se acabaron las letras o ingreso "!!". Mostrar score total y finalizar
    if handlen == 0:
        print(f'Ya no tienes más letras. Puntaje total de esta mano: {hand_score}')
    else: 
        print(f'Puntaje total de esta mano: {hand_score}')
    print('---------------------------------')

    return hand_score

## Jugando una partida

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    import re
    new_hand = hand.copy()

    # si la letra ingresada a reemplazar no esta en la mano
    # no se efectuan cambios
    if letter not in hand.keys(): 
        return new_hand

    # Si requirio el cambio de una letra que SI esta en la mano, 
    # busco una letra aleatoria para reemplazarla

    # excluyo de las letras disponibles las letras que ya tiene en la mano
    base_letters = VOWELS + CONSONANTS
    excluding_letters = ''.join(hand.keys())
    base_letters = re.sub(f'[{excluding_letters}]', "", base_letters)

    # selecciono una letra al azar, dentro de las disponibles
    new_letter = random.choice(base_letters)

    # reemplazo de la hand, la letra que se requiere por la nueva
    new_hand[new_letter] = new_hand[letter]
    del new_hand[letter]

    return new_hand

           
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    print('''📕📗📘📙 📕📗📘📙 📕📗📘📙 📕📗📘📙 📕📗📘📙
    Bienvenido al Juego de Palabras!
    ===============================
    ''')

    # preguntar cuantas manos quiere jugar
    invalid_input = True
    while invalid_input:
        try: 
            hands_to_play = input('Ingrese cuántas manos desea jugar: ')
            hands_to_play = int(hands_to_play)
            invalid_input = False
        except: 
            print('Ha ingresado un número inválido. Por favor, vuelva a intentarlo.')

    print('\nComencemos!!')
    print('-----------------------------------------------')

    # condiciones inciales
    game_score = 0
    hands_left = hands_to_play
    substitutions_left = SUBSTITUTIONS
    replays_left = REPLAYS

    # mientras haya manos por jugar
    while hands_left > 0:
        ## Repartir y mostrar mano actual
        hand = deal_hand(HAND_SIZE)
        print('Comenzamos con una nueva mano.')
        # display_hand solo se hace si quedan substitutions (xq ya esta en play_hand)

        ## preguntar si desea modificarla (en caso que le queden sustituciones disponibles)
        if substitutions_left > 0:
            print('Mano actual: ', end=" ")
            display_hand(hand)            
            want_substitute = input('Desea reemplazar alguna letra de la mano? (yes/no): ')            
            if want_substitute in ['yes', 'YES']:
                substitutions_left -= 1
                letter_want_substitute = input('Qué letra desea sustituir: ')
                hand = substitute_hand(hand, letter_want_substitute)
            print()
        
        ## jugar mano y obtener puntaje de la misma
        hand_score = play_hand(hand, word_list)

        ## preguntar si desea rejugar la misma mano (en caso que queden revanchas disponibles)
        if replays_left > 0:
            want_replay = input('Desea volver a jugar esta mano? (yes/no): ')
            print()
            if want_replay in ['yes', 'YES']:
                replays_left -= 1

                ## repite jugada con misma mano 
                # (si fue sustituida se usa esa, no la primera primera)
                # y no se puede pedir sustitucion en esta revancha
                hand_score = play_hand(hand, word_list)        

        ## sumar al puntaje total del juego
        game_score += hand_score

        ## calcular cuantas manos quedan y continuar
        hands_left -= 1
    
    # se acabaron las manos
    # devolver el puntaje total del juego
    return game_score


def exit_game():
    exit()

#
# Build data structures used for entire session and play game
if __name__ == '__main__':
    word_list = load_words()
    game_score = play_game(word_list)
    print('\n👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏')
    print(f'El juego ha finalizado. Obtuviste un PUNTAJE TOTAL: {game_score}')
    print('Hasta pronto! 👋')
