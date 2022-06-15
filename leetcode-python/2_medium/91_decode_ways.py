######### LeetCode Problem N°91 - Decode Ways (Medium) ################
# A message containing letters from A-Z can be encoded 
# into numbers using the following mapping:
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped
# back into letters using the reverse of the mapping above 
# (there may be multiple ways). For example, "11106" can be mapped into:

# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped 
# into 'F' since "6" is different from "06".
#
# Given a string s containing only digits, return the number of ways to decode it.
# The test cases are generated so that the answer fits in a 32-bit integer.
#
# Example 1:
# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
#
# Example 2:
# Input: s = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
#
# Example 3:
# Input: s = "06"
# Output: 0
# Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
#
# Constraints:
# 1 <= s.length <= 100
# s contains only digits and may contain leading zero(s).
from functools import lru_cache

class SolutionRecursive:
    @lru_cache(maxsize=None)
    def dfs(self, string:str) -> int:
        ''' 
        Número de grupos posibles de códigos, a partir de un "string".
        lru_cache: memoriza resultados para no recalcular si ya se llamó la función con un string dado
        >>> dfs('11106')
        2
        -----------
        Grupos posibles:[[1,1,1,0,6], [1,1,1,06], [1,1,10,6], [1,11,0,6], [1,11,06], [11,1,0,6], [11,1,06], [11,10,6]]
        Pero filtrando los inválidos, quedan: [[1,1,10,6], [11,10,6]]
        '''
        # no habrá grupos posibles si inicia con '0'
        if len(string)>0 and string[0]=='0': return 0

        if len(string)<=1: return 1

        # s[0:2] -> '10'/'26'....
        if int(string[:2]) <= 26:
            combs_p = self.dfs(string[1:])
            combs_pp = self.dfs(string[2:])
            return combs_p + combs_pp
        # s[0:2] -> '27'... solo sumo combinaciones tras separar '2','7....'
        else:
            return self.dfs(string[1:])

    def numDecodings(self, s: str) -> int:
        if not s: return 0
        return self.dfs(s)   

class SolutionDP:
    def numDecodings(self, s: str) -> int: 
        if not s: return 0
        n = len(s)

        # dp[i] -> solución para s[:i]
        dp = [0]*(n+1)
        dp[0] = 1 # para salvar caso de s[:2]
        dp[1] = 1 if s[0] != '0' else 0

        for i in range(2, n+1):
            # si todos los codigos fueran validos dp[i] = dp[i-1] + dp[i-2]
            # pero debo filtrar, solo sumar si son códigos válidos
            print(s, s[i-1])
            dp[i] = dp[i-1] if s[i-1] != '0' else 0
            dp[i] += dp[i-2] if 10 <= int(s[i-2:i]) <= 26 else 0

        return dp[n]        

test1={'code': '11106', 'out_exp': 2}
test2={'code': '12', 'out_exp': 2}
test3={'code': '26', 'out_exp': 2}
test4={'code': '06', 'out_exp': 0}
test5={'code': '1111111111111111111111111111', 'out_exp': 0}
test6={'code': '0', 'out_exp': 0}
test7={'code': '106', 'out_exp': 1}
tests = [test2]

for test in tests:
    res = SolutionDP().numDecodings(test['code'])
    print('code:', test['code'], 'Resultado esperado:', test['out_exp'], 'Resultado:', res)
