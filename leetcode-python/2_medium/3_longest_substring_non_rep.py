######### LeetCode Problem N°3 - Longest substring without repeating chars (Medium) ################
# Given a string s, find the length of the longest 
# substring without repeating characters.
#
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
# Constraints:
# 0 <= s.length <= 5 * 10**4
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''Tamano del mayor substring sin caracteres repetidos'''
        # casos edge
        if not s: return 0
        if len(s) == 1: return 1
        
        res, sub = 1, [s[0]]
        for i in range(1, len(s)):
            try:
                # Si el char esta en el sub, deja de sumar...
                ind = sub.index(s[i])
                res = max(len(sub), res)
                # y ahora sub se toma desde la ocurrencia anterior del char
                sub = sub[ind+1:]
                sub.append(s[i])
            except:
                sub.append(s[i])

        res = max(len(sub), res)
        return res

class SolutionFast:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''Tamano del mayor substring sin caracteres repetidos'''
        start, max_len = 0, 0
        # chars usados y su indice
        used_chars = {}

        for i, c in enumerate(s):
            if c in used_chars and start <= used_chars[c]:
                # char repetido, actualizo start a su ant ocurrencia + 1
                start = used_chars[c] + 1
            else:
                max_len = max(max_len, i - start + 1)
            # guardo el índice del caracter 
            used_chars[c] = i
            
        return max_len

# Pruebas
test1 = {'s': 'abcabcbb', 'output_exp': 3}
test2 = {'s': 'bbbbb', 'output_exp': 1}
test3 = {'s': 'pwwkew', 'output_exp': 3}
test4 = {'s': 'dvdf', 'output_exp': 3}
test4 = {'s': '1234567890532100abcd5efghij', 'output_exp': 12}
tests = [test1, test2, test3, test4]
tests = [test4]
for test in tests:
    res = SolutionFast().lengthOfLongestSubstring(test['s'])
    print('s: {} - Resultado esperado: {} - Resultado: {}'.format(test['s'], test['output_exp'], res))        