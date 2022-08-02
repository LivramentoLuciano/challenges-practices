######### LeetCode Problem N°395 - Longest Substring With At Least K Repeating Characters (Medium) ################
# Given a string s and an integer k, return the length of the longest substring of s such 
# that the frequency of each character in this substring is greater than or equal to k.
#
# Example 1:
# Input: s = "aaabb", k = 3
# Output: 3
# Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
#
# Example 2:
# Input: s = "ababbc", k = 2
# Output: 5
# Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
#
# Constraints:
# 1 <= s.length <= 10**4
# s consists of only lowercase English letters.
# 1 <= k <= 10**5

class Solution:
    '''Solución más rápida'''
    def longestSubstring(self, s: str, k: int) -> int:
        # Algoritmo:
        # El concepto basico es que si alguna de las letras no está repetida
        # K o más veces, entonces, ningún substring que contenga dicha letra
        # cumplirá la condición. Por tanto se realiza una recursión para aquellos
        # substrings que no contengan dicha letra.
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(sub, k) for sub in s.split(c))

        return len(s)


from collections import Counter
class SolutionCounter:
    def longestSubstring(self, s: str, k: int) -> int:
        # Algoritmo:
        # El principio es el mismo que el anterior, si alguna letra no cumple
        # la condición de ocurrencias, se aplica recursividad sobre los substrings que
        # no incluyan dicho caracter
        counter = Counter(s)
        for c, count in counter.items():
            if count < k:
                return max(self.longestSubstring(sub,k) for sub in s.split(c))

        return len(s)

# Pruebas
test1 = {'s': 'aaabb', 'k': 3, 'output_exp': 3}
test2 = {'s': 'ababbc', 'k': 2, 'output_exp': 5}
tests = [test1, test2]
tests = [test2] 
for test in tests:
    res = Solution().longestSubstring(test['s'], test['k'])
    print('s: {}, k: {} - Resultado esperado: {} - Resultado: {}'.format(test['s'], test['k'], test['output_exp'], res))