######### LeetCode Problem N°5 - Longest palindromic substring (Medium) ################
# Given a string s, return the longest palindromic substring in s.
#
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#
# Example 2:
# Input: s = "cbbd"
# Output: "bb"
#
# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''Palíndromo más largo dentro de un string'''
        # algoritmo:
        #   - desde el centro agregando los caracteres laterales y verifico si es palindromo
        #     hasta extremos (primer y último caracter)
        #   - ese "centro" lo voy iterando, es decir, tomo como "centro" desde el primer hasta el 
        #     último caracter (sobre cada uno realizo la busqueda de palindromos con los laterales)
        #   - Si el string es impar, los caracteres laterales de inicio serán el mismo caracter central
        # casos base
        if not s: return ""

        longest = ""
        for i in range(len(s)):
            # maximo palindromo centrado en 'i', impar
            res = self.helper(s, i, i)
            if len(res) > len(longest): 
                longest = res

            # maximo palindromo centrado en 'i', 'i+1', par
            res = self.helper(s, i, i+1)
            if len(res) > len(longest):
                longest = res
        
        return longest

    def helper(self, s:str, l:int, r:int) -> bool:
        '''Desde el interior hacia el exterior, devuelve el máximo palindromo'''
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        
        return s[l+1:r]
           
# NOTE: Solución Mediante Dynamic Programming (más lenta)           
class SolutionDP:
    def longestPalindrome(self, s: str) -> str:
        '''Palíndromo más largo dentro de un string, mediante Dynamic Programming'''
        # algoritmo:
        #   - dp[i][j] -> indica si el string[i:j] es palindromo

        # casos edge
        if not s: return ""

        # inicialmente todos False, y los dp[i][i] True 
        # (stirng de un único caracter es palindromo)
        n = len(s)
        dp = [[False]*n for x in range(n)]
        for start in range(n):
            dp[start][start] = True
        
        # construyo la tabla dinamica de palíndromos s[i][j]
        # se debe recorrer de menor substring a mayores (inverso)
        longest = s[0]
        for end in range(1, n):
            for start in range(end):
                print(f'start,end:({start},{end}) - (s[start], s[end]): ({s[start]},{s[end]})')
                if s[start] == s[end]:
                    print('s[start]=s[end]', end=' ')
                    # si el char de inicio y fin son iguales 
                    # Y es de 2 chars o la palabra interior es palindromo
                    if (end == start+1) or dp[start+1][end-1]:
                        print('s[start:end+1]', s[start:end+1], 'es de 2 caracteres o su interior es palindromo', end=' ')
                        dp[start][end] = True
                        if (end-start+1) > len(longest):
                            print('. Además, es mas largo que', longest, '-> lo reemplazo.')
                            longest = s[start:end+1]
                        else: print()
                    else: print('s[start:end+1]', s[start:end+1], 'no es de 2 caracteres ni su interior es palindromo')
        return longest


# Pruebas
test1 = {'s': 'babad', 'output_exp': 'bab'}
test2 = {'s': 'cbbd', 'output_exp': 'bb'}
test3 = {'s': 'aaaa', 'output_exp': 'aaaa'}
tests = [test1, test2, test3]
for test in tests:
    res = Solution().longestPalindrome(test['s'])
    print('s: {} - Resultado esperado: {} - Resultado: {}'.format(test['s'], test['output_exp'], res))    