############ LeetCode Problem N° 104: Maximum depth of Binary Tree (Easy) #################
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the 
# longest path from the root node down to the farthest leaf node.
#
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
#
# Example 2:
# Input: root = [1,null,2]
# Output: 2
#
# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Nodo(val:{self.val}, left: {self.left}, right: {self.right})'      

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        '''
        Dada la raiz de un Binary Tree, devuelve su profundidad máxima.
        >>> maxDepth(TreeNode(3,TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
        3
        '''
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# Pruebas
test1 = {'root': TreeNode(3,TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), 'output_exp': 3}
test2 = {'root': TreeNode(1, None, TreeNode(2)), 'output_exp': 2}
tests = [test1, test2]
for test in tests:
    res = Solution().maxDepth(test['root'])
    print('root: {} - Resultado esperado: {} - Resultado: {}'\
        .format(test['root'], test['output_exp'], res))  