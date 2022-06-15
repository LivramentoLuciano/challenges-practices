######### LeetCode Problem N°2 - Add Two Numbers (Medium) ################
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain 
# any leading zero, except the number 0 itself.
#
# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# 
# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#
# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'Nodo({self.val}, next:{self.next})'

class Solution:
    def __init__(self):
        self.CARRY_NODE = ListNode(1, None)

    def add_two_digits(self, d1:int, d2:int) ->tuple[int]:
        '''
        Realiza la suma de dos números de base decimal,
        Devuelve el dígito resultante y carry ("5+8=13, me llevo 1")
        
        >>> add_digits(5,8)
        (3,1)
        '''
        carry = 0
        res = d1 + d2
        if d1 + d2 >= 10: 
            res -= 10
            carry = 1
        return (res,carry)

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) ->ListNode:
        '''
        Dados 2 números (base decimal) expresados como linked-list (nodos anidados), 
        realiza la suma de ambos y entrega el resultado, expresado de la misma forma.

        >>> l1 = ListNode(2, ListNode(4, ListNode(3, None)))
        >>> l2 = ListNode(5, ListNode(6, ListNode(4, None)))
        >>> addTwoNumbers(l1, l2)
        ListNode(7, ListNode(0, ListNode(8, None)))
        '''
        # caso base, un Nodo vacio (o ambos)
        # -> ListNode(6, Nodo(1,None)) + None = ListNode(6,ListNode(1,None)
        # (cuando un numero tiene mas digitos que el otro, en la recursividad, 
        #  llegara el caso que uno de los numeros ya no tenga mas nodos para sumar)
        if not l1: return l2
        if not l2: return l1
        
        # sumo de a 1 digito (val) de cada nodo
        node_sum, carry = self.add_two_digits(l1.val, l2.val)

        # Si la suma arroja un carry: sig digito será la suma del digito siguiente de c/numero + el carry
        # Sino: sig digito será la suma del digito siguiente de c/numero
        if carry == 1:
            result = ListNode(node_sum, self.addTwoNumbers(self.addTwoNumbers(l1.next, l2.next),self.CARRY_NODE))
            return result
        else:
            result = ListNode(node_sum, self.addTwoNumbers(l1.next, l2.next))
            return result


# Pruebas
test1 = {
    'l1': ListNode(2, ListNode(4, ListNode(3, None))), 
    'l2':ListNode(5, ListNode(6, ListNode(4, None))), 
    'output_exp': ListNode(7, ListNode(0, ListNode(8, None)))
}   
test2 = {
    'l1': ListNode(6, None), 
    'l2':ListNode(5, None), 
    'output_exp': ListNode(1, ListNode(1,None))
}  
test3 = {
    'l1': ListNode(5, ListNode(5, None)), 
    'l2':ListNode(5, ListNode(5, None)), 
    'output_exp': ListNode(0, ListNode(1,ListNode(1,None)))
}    

tests = [test3]
for test in tests:
    res = Solution().addTwoNumbers(test['l1'], test['l2'])
    print('l1: {}\nl2: {}\nResultado esperado: {}\nResultado: {}'\
        .format(test['l1'], test['l2'], test['output_exp'], res)) 
    print()
 