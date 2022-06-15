####### LeetCode Problem N° 20: Valid Parenthesis (Easy) ################
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# - Open brackets must be closed by the same type of brackets.
# - Open brackets must be closed in the correct order.
#
# Example 1:
# Input: s = "()"
# Output: true
#
# Example 2:
# Input: s = "()[]{}"
# Output: true
#
# Example 3:
# Input: s = "(]"
# Output: false
#
# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False        

        while s:
            if '()' in s:
                s = s.replace('()', '')
            elif '[]' in s:
                s = s.replace('[]', '')
            elif '{}' in s:
                s = s.replace('{}', '')
            else:
                return False
        return True

# TODO: Resolver utilizando el metodo de stackear las llaves de apertura
#       y matchear con las de cierre -> [https://favtutor.com/blogs/valid-parentheses]


test1 = { 's': '()','output_exp': True }
test2 = { 's': '()[]{}','output_exp': True }
test3 = { 's': '(]','output_exp': False }
test4 = { 's': '}}','output_exp': False }
test5 = { 's': '{[]}', 'output_exp': True }
tests = [test1, test2, test3, test4, test5]

for test in tests:
    res = Solution().isValid(test['s'])
    print('Input: {}\tResultado esperado: {}\tResultado: {}'\
        .format(test['s'], test['output_exp'], res))