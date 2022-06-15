######### LeetCode Problem N°242 - Valid Anagram (Easy) ################
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different 
# word or phrase, typically using all the original letters exactly once.
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
#
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#
# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
#
# Follow up: What if the inputs contain Unicode characters? 
# How would you adapt your solution to such a case?

from collections import Counter
class SolutionDict:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Devuelve True si ambos string son anagramas (contienen las 
        mismas letras, la misma cantidad de veces).
        '''
        # Creo un diccionario con las ocurrencias de cada letra de s y t
        # Luego, los comparo
        counter_s = Counter(s)
        counter_t = Counter(t)
        return counter_s == counter_t

class SolutionDictFaster:
    def isAnagram(self, s: str, t: str) -> bool:
        '''Variante uso de un único Diccionario Counter'''
        # Cargo con las ocurrencias de letras en s, 
        # le resto las de t y si quedaron todas en 0, Ok
        count = Counter(s)
        for x in t: count[x] -= 1
        return all([ x==0 for x in count.values() ])

class SolutionSort:
    def isAnagram(self, s: str, t: str) -> bool:
        ''' Basado en método Sorted '''
        return sorted(s) == sorted(t)

# Pruebas
test1 = {'s': 'anagram', 't': 'nagaram', 'output_exp': True}
test2 = {'s': 'ab', 't': 'a', 'output_exp': False}
test2 = {'s': 'a', 't': 'ab', 'output_exp': False}
tests = [test2]
for test in tests:
    res = SolutionDictFaster().isAnagram(test['s'], test['t'])
    print('s: {}, t: {}\tResultado esperado: {}\tResultado: {}'\
        .format(test['s'], test['t'], test['output_exp'], res))    
