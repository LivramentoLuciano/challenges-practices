######### LeetCode Problem N°387 - First unique char (Easy) ################
# Given a string s, find the first non-repeating character 
# in it and return its index. If it does not exist, return -1.
#
# Example 1:
# Input: s = "leetcode"
# Output: 0
#
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
#
# Example 3:
# Input: s = "aabb"
# Output: -1
#
# Constraints:
# 1 <= s.length <= 105
# s consists of only lowercase English letters.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Ocurrencias de cada letra
        count = {}
        for l in s: 
            count[l] = count.get(l, 0) + 1
        
        # Si no hay al menos una que sea Unique
        if not any([cnt==1 for cnt in count.values()]):
            return -1
        
        # Indice primera ocurrencia del primer caracter unique
        for l, cnt in count.items():
            if cnt == 1: 
                return s.find(l)