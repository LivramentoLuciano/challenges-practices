######### LeetCode Problem N°236 - Lowest Common Ancestor (Medium) ################
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined 
# between two nodes p and q as the lowest node in T that has both p and q as descendants 
# (where we allow a node to be a descendant of itself).”
#
# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
#
# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
#
# Example 3:
# Input: root = [1,2], p = 1, q = 2
# Output: 1
#
# Constraints:
#   - The number of nodes in the tree is in the range [2, 105].
#   - -10**9 <= Node.val <= 10**9
#   - All Node.val are unique.
#   - p != q
#   - p and q will exist in the tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self): 
        return f'N({self.val})'

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Algoritmo:
        # Recorro todo el root, y guardo path hasta p y q
        # Después, busco en ambos path, el parent común más cercano a p y q
        p_path, q_path = self.path(root, p, q)

        # recorro ambos path buscando el LCA
        for i in range(len(p_path)):
            for j in range(len(q_path)):
                if p_path[~i].val == q_path[~j].val:
                    return p_path[~i]

        return None

    def path(self, root:TreeNode, n:TreeNode, n2:TreeNode):
        stack, n_path, n2_path = [], [], []
        while True:
            if root.left:
                stack.append(root)
                root.left, root = None, root.left
            elif root.right:
                stack.append(root)
                root.right, root = None, root.right
            else:
                if root.val == n.val:
                    n_path = stack[:]
                    n_path.append(root)
                if root.val == n2.val:
                    n2_path = stack[:]
                    n2_path.append(root)
                if n_path and n2_path:
                    break 
                root = stack.pop()

        return (n_path, n2_path)

test1 = { 
    'root': TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8))), 
    'p': TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
    'q': TreeNode(1, TreeNode(0), TreeNode(8)),
    'out_exp': TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
}
test2 = { 
    'root': TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8))), 
    'p': TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
    'q': TreeNode(4),
    'out_exp': TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
}
test3 = { 
    'root': TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8))), 
    'p': TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
    'q': TreeNode(1, TreeNode(0), TreeNode(8)),
    'out_exp': TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
}

tests = [test2]
for test in tests:
    res = Solution().lowestCommonAncestor(test['root'], test['p'], test['q'])
    print('Root:', test['root'])
    print('p:', test['p'])
    print('q:', test['q'])
    print('Resultado esperado: ', test['out_exp'])
    print('Resultado:', res)
    print('-'*75)
