######### LeetCode Problem N°139 - Word Break (Medium) ################
# Given a string s and a dictionary of strings wordDict, return true 
# if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
#
# Example 1:
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
#
# Example 2:
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
#
# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
#
# Constraints:
# - 1 <= s.length <= 300
# - 1 <= wordDict.length <= 1000
# - 1 <= wordDict[i].length <= 20
# - s and wordDict[i] consist of only lowercase English letters.
# - All the strings of wordDict are unique.

from collections import deque
class SolutionIterative:
    '''Solución Iterando'''
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # Algoritmo
        # Por cada word del diccionario, reviso si el string 
        # comienza con ella, y agrego el resto del string a una 
        # cola que va a ir realizando el mismo proceso hasta encontrar
        # un empty_string, en caso de que la palabra pueda ser wordBreak
        # o se acabarán los substring de la cola y retornará Falso
        q = deque([s])
        seen = set()
        while q:
            s = q.popleft()
            for word in wordDict:
                if s.startswith(word):
                    subs = s[len(word):]
                    if subs == '':
                        # Llegó al final quebrando s en las distintas word -> OK
                        return True

                    if subs not in seen:
                        q.append(subs)
                        seen.add(subs)
        return False

class SolutionDP:
    '''Solución aplicando Dynamic Programming'''
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # Algoritmo, a través de una tabla dp
        # dp[i] -> Indica si es posible quebrar s[:i] en diferentes word (del wordDict)
        # El punto clave está en recorrer 's' con 2 loops, el principal (i) recorre s completo
        # y el segundo (j), recorre de 0 a 'i', planteando que dp[i] será verdadero:
        #   - Si dp[j] es verdadero (es posible quebrar la palabra hasta el índice j)
        #   - Y Si s[j:i] es una palabra dentro del diccionario        
        
        # Casos base
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[n]


# Pruebas
test1={'s': 'leetcode', 'wordDict': ["leet","code"], 'out_exp': True}
test2={'s': 'applepenapple', 'wordDict': ["apple","pen"], 'out_exp': True}
test3={'s': 'catsandog', 'wordDict': ["cats","dog","sand","and","cat"], 'out_exp': False}
test4={'s': 'cars', 'wordDict': ["car","ca","rs"], 'out_exp': True}
test5={'s': 'carsb', 'wordDict': ["car","cars", 'b'], 'out_exp': True}
test6 = {
    's': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab',
    'wordDict': ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"],
    'out_exp': False
}
tests = [test1,test2, test3, test4]
for test in tests:
    res = SolutionDP().wordBreak(test['s'], test['wordDict'])
    print('s: {}, Dict: {} - Resultado esperado: {} - Resultado: {}'.format(test['s'], test['wordDict'], test['out_exp'], res))