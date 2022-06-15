######### LeetCode Problem N°17 - Letters phone Number (Medium) ################
# Given a string containing digits from 2-9 inclusive, 
# return all possible letter combinations that the 
# number could represent. Return the answer in any order.
#
# A mapping of digit to letters (just like on the telephone buttons) 
# is given below. Note that 1 does not map to any letters.
#
# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
# Example 2:
# Input: digits = ""
# Output: []
#
# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]
#
# Constraints:
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

class Solution:
    def __init__(self):
        self.DIGIT_LETTERS = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }    

    def insert_char(self, char:str, words:list[str]) ->list[str]:
        '''Combina el char con las distintas words. Ejemplo:
        >>> insert_char('a', ['d', 'e', 'f'])
        ['ad', 'ae', 'af']

        >>> insert_char('a', ['ad','ae','af','bd','be','bf','cd','ce','cf'])
        ['aad','aae','aaf','abd','abe','abf','acd','ace','acf']
        '''
        res = []
        for word in words:
            res.append(char+word)        
        return res

    def letterCombinations(self, digits: str) -> list[str]:
        '''
        Aplicando recursividad, combino las distintas letras referidas al primer digito,
        con las combinaciones resultantes del resto de digitos.
        Ejemplo: digits='23'
        1) entries = ['abc', 'def'] -> Combinar cada letra de 'abc' con las combinaciones 
                                       resultantes del resto de las entradas ['def']
        2) entries = ['def']        -> caso base, las combinaciones posibles son simplemente ['d', 'e', 'f']
        3) retorna y combina:       -> 'a' -> ['ad', 'ae', 'af']
                                    -> 'b' -> ['bd', 'be', 'bf']
                                    -> 'c' -> ['cd', 'ce', 'cf']
                                    -> combinations = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']                                          
        '''
        # Caso vacio
        if not digits: return []
        
        # caso base, 1 digito -> entries=['def'], combinaciones=['d', 'e', 'f']
        if len(digits) == 1:
            return list(self.DIGIT_LETTERS[digits[0]])

        # ej, digits: '23', entries=['abc', 'def']
        entries = [ self.DIGIT_LETTERS[digit] for digit in digits]

        # agregar c/char de la primera entry, 
        # a cada combinacion resultante del resto de entries
        prev_combinations = self.letterCombinations(digits[1:])
        combinations = []
        for char in entries[0]:
            combinations.extend(self.insert_char(char, prev_combinations))
        return combinations

# Pruebas
test1 = {'digits': '23', 'output_exp': ['ad','ae','af','bd','be','bf','cd','ce','cf']}
test2 = {'digits': '234', 'output_exp': ['adg','adh','adi','aeg','aeh','aei','afg','afh','afi',\
                                         'bdg','bdh','bdi','beg','beh','bei','bfg','bfh','bfi',\
                                         'cdg','cdh','cdi','ceg','ceh','cei','cfg','cfh','cfi']}
test3 = {'digits': '223', 'output_exp': ['aad','aae','aaf','abd','abe','abf','acd','ace','acf',\
                                         'bad','bae','baf','bbd','bbe','bbf','bcd','bce','bcf',\
                                         'cad','cae','caf','cbd','cbe','cbf','ccd','cce','ccf',]}                                     

tests = [test3]
for test in tests:
    res = Solution().letterCombinations(test['digits'])
    print('digits: {}\nResultado esperado: {}\nResultado: {}'\
        .format(test['digits'], test['output_exp'], res))  
