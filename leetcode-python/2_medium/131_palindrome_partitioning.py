######### LeetCode Problem N°131 - Palindrome Partitioning (Medium) ################
# Given a string s, partition s such that every substring 
# of the partition is a palindrome. Return all possible palindrome partitioning of s.
# A palindrome string is a string that reads the same backward as forward.
#
# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
#
# Example 2:
# Input: s = "a"
# Output: [["a"]]
#
# Constraints:
# 1 <= s.length <= 16
# s contains only lowercase English letters.

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        # Las particiones posibles dado un s[:i] serán todas las particiones
        # del s[:i-1], combinadas con el caracter s[i-1] donde esta está formada por:
        # - dp[i-1], s[i] (agrego a cada partición (lista, append) el elemento s[i])
        # - s[i] pegado al último elemento (substring) de cada partición de dp[i-1] 
        
        # casos base
        if not s: return []
        if len(s) == 1: return [[s]]

        # dp[i] -> todas las particiones posibles de s[:i]
        dp = [[] for _ in range(len(s)+1)]
        dp[1] = [[s[0]]]

        for i in range(2, len(s)+1):
            for part in dp[i-1]:
                dp[i].extend([part + [s[i-1]], part[:-1] + [part[-1]+s[i-1]]])
            
        palindromes = self.filter_palindromes(dp[-1])
        return palindromes
    
    def filter_palindromes(self, partitions: list[list[str]]) -> list[list[str]]:
        '''Dada la lista de particiones posibles, devuelve solo aquellas donde todas sean palindromos'''
        palindromes_partitions = []
        for partition in partitions:
            palindromes = [ sub == sub[::-1] for sub in partition ]
            if all(palindromes):
                palindromes_partitions.append(partition)
        return palindromes_partitions

# Pruebas
test1 = {'s': 'aab', 'output_exp': [['a','a','b'],['aa','b']]}
test2 = {'s': 'a', 'output_exp': [['a']]}
test3 = {'s': 'abbab', 'output_exp': [['a']]}
test3 = {'s': 'efe', 'output_exp': [["e","f","e"],["efe"]]}
tests = [test1, test2]
tests = [test3]
for test in tests:
    res = Solution().partition(test['s'])
    print('s: {} - Resultado esperado: {} - Resultado: {}'.format(test['s'], test['output_exp'], res))            