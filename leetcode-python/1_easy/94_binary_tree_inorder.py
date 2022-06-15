########## LeetCode Problem N°99 - Binary Tree Inorder (Easy) ################
# Given the root of a binary tree, return the 
# inorder traversal of its nodes' values.
#
# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]
#
# Example 2:
# Input: root = []
# Output: []
#
# Example 3:
# Input: root = [1]
# Output: [1]
#
# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Nodo({self.val}, izq:{self.left}, der: {self.right})'        

class Solution:
    def dft(self, root: TreeNode) -> list[int]:
        '''Recorrido DFT básico del arbol de nodos'''
        stack = [root]
        path = []
        while len(stack) > 0:
            current = stack.pop()
            print('Current Node:', current)
            path.append(current.val)
            neighbors = [ neighbor for neighbor in [current.left, current.right] if neighbor != None]
            for neighbor in neighbors:
                stack.append(neighbor)
                    
        return path


    def inorderTraversal(self, root: TreeNode) -> list[int]:
        '''Recorrido DFT Inorder Traversal del árbol de nodos'''
        # caso nulo
        if not root: return []

        stack, path = [], []        
        current = root

        while True:
            while current != None:
                # stackea todos los left
                stack.append(current)
                current = current.left

            # llego al ultimo de la izquierda
            # procesa y va hacia su derecha
            if not stack: return path
            node = stack.pop()
            path.append(node.val)
            current = node.right

test1 = { 'root': TreeNode(1, None, TreeNode(2, TreeNode(3))), 'out_exp': [1,3,2] }
test2 = { 'root': TreeNode(1), 'out_exp': [1] }
test3 = { 'root': [], 'out_exp': [] }
tests = [test1, test2, test3]

for test in tests:
    res = Solution().inorderTraversal(test['root'])
    print('Root:', test['root'])
    print('Resultado esperado: ', test['out_exp'])
    print('Resultado:', res)
    print('-'*75)