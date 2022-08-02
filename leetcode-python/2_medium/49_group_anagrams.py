######### LeetCode Problem N°49 - Group Anagrams (Medium) ################
# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order. An Anagram is a word 
# or phrase formed by rearranging the letters of a different 
# word or phrase, typically using all the original letters exactly once.
#
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# Example 2:
# Input: strs = [""]
# Output: [[""]]
#
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
#
# Constraints:
# 1 <= strs.length <= 10**4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        '''
        Dada una lista de strings, devuelve una lista con grupos de estos
        que sean anagramas.
        >>> groupAnagrams(["eat","tea","tan","ate","nat","bat"])
        [["bat"],["nat","tan"],["ate","eat","tea"]]
        '''
        # Algoritmo:
        # La solución adecuada, resulta de encararlo ligeramente diferente a la DP
        # Construyo un diccionario donde iré guardando los anagramas, para poder hacerlo
        # debo saber cuando 2 palabras son anagramas, entonces, me baso en que lo serán si
        # ambas son iguales a una 'keyword' que será la palabra ordenada (sorted)
        # Ejemplo: 'tea' ->  sorted: 'aet' --- Luego si tengo la palabra 'ate' -> sorted: 'aet'
        # y por tanto son anagramas. 
        # De esta manera, puedo recorrer una sola vez toda la lista de strings y en cada paso
        # ir agrupando los anagramas
        anagrams = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            anagrams[sorted_s] = anagrams.get(sorted_s, []) + [s]

        return anagrams.values()

# Pruebas
test1={'strs': ['eat','tea','tan','ate','nat','bat'], 'out_exp': [['bat'],['nat','tan'],['ate','eat','tea']]}
test2={'strs': [''], 'out_exp': [['']]}
test3={'strs': ["a"], 'out_exp': [["a"]]}
tests = [test1,test2, test3]
tests = [test1]
for test in tests:
    res = Solution().groupAnagrams(test['strs'])
    print('strs: {} - Resultado esperado: {} - Resultado: {}'.format(test['strs'], test['out_exp'], res))