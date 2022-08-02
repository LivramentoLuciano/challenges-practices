######### LeetCode Problem N°21 - Merge Two Sorted Lists (Easy) ################
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by 
# splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
#
# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
# Example 2:
# Input: list1 = [], list2 = []
# Output: []
#
# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]
#
# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

## Visualización Algoritmo Resolución
# INICIO:
# l1 ---> val: 1
#                  next: ---> val:2
#                             next: ---> 
# res ---> 
# cur ---> val: 0
#          next: None
#
# COMP: l1.val < l2.val (True) 
# Entonces cur.next = l1
# res/cur ---> val: 0
#              next: ---> val: 1
#                         next: ---> val:2
#                                    next: ---> ...
# Luego, cur = l1
# cur ---> val: 1
#          next: ---> val: 2
#                     next: ---> ...
#
# Y l1 = l1.next
# l1 ---> val:2
#         next: ---> ...
#
# QUEDANDO:
# res ---> val: 0
#          next: ---> val: 1
#                ^    next: ---> val:2
#          cur __|         ^     next: ---> ...
#                      l1__|
#
# Sucesivamente, hasta que no haya elementos en l1 o l2
# El Resultado queda alojado en res.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'Nodo(val: {self.val}, next: {self.next})'

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        '''
        Dadas 2 Listas de Nodos ordenadas, entrega la combinación de ambas,
        también ordenada (ascendente).

        >>> mergeTwoLists(ListNode(1, ListNode(2, ListNode(4, None))), ListNode(1, ListNode(2, ListNode(4, None))))
        ListNode(1,ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, None)))))),
        '''
        # casos base
        if not list1: return list2
        if not list2: return list1            

        # l1 y l2, simplemente para no modificar list1, list2
        l1, l2 = list1, list2
        res = cur = ListNode()

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                cur = l1
                l1 = l1.next
            else: 
                cur.next = l2
                cur = l2
                l2 = l2.next

        # la lista que siga teniendo nodos, apunto allí
        if l1 or l2:
            cur.next = l1 if l1 else l2
        
        return res.next

# Pruebas
test1 = {
    'list1': ListNode(1, ListNode(2, ListNode(4, None))), 
    'list2': ListNode(1, ListNode(3, ListNode(4, None))), 
    'output_exp': ListNode(1,ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, None)))))),
}
test2 = {
    'list1': None, 
    'list2': None, 
    'output_exp': None
}
test3 = {
    'list1': None, 
    'list2': ListNode(0), 
    'output_exp': ListNode(0)
}
tests = [test1, test2, test3]
for test in tests:
    res = Solution().mergeTwoLists(test['list1'], test['list2'])
    print('list1: {}, list2: {}\nResultado esperado: {}\nResultado: {}'\
        .format(test['list1'], test['list2'], test['output_exp'], res))            