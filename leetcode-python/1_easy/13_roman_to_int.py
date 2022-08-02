############ LeetCode Problem N° 13: Roman To Integer (Easy) #################
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together.
# 12 is written as XII, which is simply X + II. 
# The number 27 is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. 
# However, the numeral for four is not IIII. Instead, the number four is written as IV. 
# Because the one is before the five we subtract it making four. 
# The same principle applies to the number nine, which is written as IX. 
#
# There are six instances where subtraction is used:
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.
#
# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
#
# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
#
# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
# Constraints:
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# # It is guaranteed that s is a valid roman numeral in the range [1, 3999].

class Solution:
    '''Solución inicial mediante condicionales'''
    def romanToInt(self, s: str) -> int:
        ROMAN_DICT = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
        res = 0
        for i in range(len(s)):
            if i == 0: res += ROMAN_DICT[s[i]]
            elif (s[i] == 'V' or s[i] == 'X') and s[i-1] == 'I': res += ROMAN_DICT[s[i]] - 2
            elif (s[i] == 'L' or s[i] == 'C') and s[i-1] == 'X': res += ROMAN_DICT[s[i]] - 20
            elif (s[i] == 'D' or s[i] == 'M') and s[i-1] == 'C': res += ROMAN_DICT[s[i]] - 200
            else: res += ROMAN_DICT[s[i]]
        return res

class SolutionReplace:
    '''
    Solución utilizando replace de Str cuando encuentre patrones de substracción,
    como "IX" (se reemplaza por "VIIII"), "XC", "CM", etc. Luego, realiza una sumatoria normal.
    '''
    def romanToInt(self, s: str) -> int:
        ROMAN_DICT = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
        REPLACEMENTS = {
            'IV': 'IIII',
            'IX': 'VIIII',
            'XL': 'XXXX',
            'XC': 'LXXXX',
            'CD': 'CCCC',
            'CM': 'DCCCC',
        }
        res = 0
        for r in REPLACEMENTS: 
            s = s.replace(r, REPLACEMENTS[r])
        for char in s:
            res += ROMAN_DICT[char]
        return res

# Pruebas
test1 = {'s': "III", 'output_exp': 3}
test2 = {'s': "LVIII", 'output_exp': 58}
test2 = {'s': "MCMXCIV", 'output_exp': 1994}
tests = [test2]
for test in tests:
    res = SolutionReplace().romanToInt(test['s'])
    print('s: {} - Resultado esperado: {} - Resultado: {}'\
        .format(test['s'], test['output_exp'], res))    