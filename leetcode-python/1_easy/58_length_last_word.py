######### LeetCode Problem N°5 - Length of Last Word (Easy) ################
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
#
# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
#
# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
#
# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
#
# Constraints:
# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # casos edge
        if not s: return 0

        # Remuevo leading, trailing whitespaces y duplicados internos
        # Lo puedo hacer todo con 'split' solo, ya que ademas de separar en los espacios
        # tambien elimina las palabras vacias
        words = s.split()
        lastword = words[-1]
        return len(lastword)


# Pruebas
test1 = {'s': "Hello World", 'output_exp': 5}
test2 = {'s': "   fly me   to   the moon  ", 'output_exp': 4}
test3 = {'s': "luffy is still joyboy", 'output_exp': 6}
tests = [test1, test2, test3]
for test in tests:
    res = Solution().lengthOfLastWord(test['s'])
    print('Input: {}\tResultado esperado: {}\tResultado: {}'\
        .format(test['s'], test['output_exp'], res))     
