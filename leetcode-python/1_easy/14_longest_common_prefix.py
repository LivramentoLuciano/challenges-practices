######### LeetCode Problem N°14 - Longest Common Prefix (Easy) ################
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortest = min(strs, key=len)
        shortest_len = len(shortest)
        if shortest_len == 0: return ""

        # recorro el menor string comparando cada char con los del resto
        # hasta encontrar uno distinto
        for i in range(shortest_len):
            for s in strs:
                if s[i] != shortest[i]:
                    return shortest[:i]
        
        return shortest

# Pruebas
test1 = {'strs': ['flower','flow','flight'], 'output_exp': 'fl'}
test2 = {'strs': ['dog','racecar','car'], 'output_exp': ''}
test3 = {'strs': [''], 'output_exp': ''}
test4 = {'strs': ['a'], 'output_exp': 'a'}
tests = [test1, test2, test3, test4]
for test in tests:
    res = Solution().longestCommonPrefix(test['strs'])
    print('s: {} - Resultado esperado: {} - Resultado: {}'\
        .format(test['strs'], test['output_exp'], res))    