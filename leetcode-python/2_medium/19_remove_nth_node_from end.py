######### LeetCode Problem N°19 - Remove Nth Node From End of the Linked List (Medium) ################
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#
# Example 2:
# Input: head = [1], n = 1
# Output: []
#
# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]
#
# Constraints:
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'Nodo(val: {self.val}, next: {self.next})'

class Solution: 
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''
        Remueve el elemento n-esimo desde el final de una LinkedList
        >>> head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
        >>> n = 2
        >>> removeNthFromEnd(head, n)
        ListNode(1, ListNode(2, ListNode(3, ListNode(5, None))))
        '''           
        fast = slow = head

        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        # slow queda en el anterior al Nth
        # reemplazo su next (el Nth) por el subsiguiente
        slow.next = slow.next.next
        return head

class SolutionA:                
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # primero obtengo el tamaño de la lista
        aux, list_len = head, 0
        while aux:
            aux = aux.next
            list_len += 1

        # si es len=n, devuelvo directamente el head.next (omito el Nth)
        if list_len == n : return head.next

        # sino, recorro hasta el nth-1 
        # y hago que su next, apunte al subsiguiente (omito el Nth)
        aux = head
        for _ in range(1, list_len - n):
            aux = aux.next

        aux.next = aux.next.next
        return head                
            
# Pruebas
test1 = {
    'head': ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))),
    'n': 2,
    'output_exp': ListNode(1, ListNode(2, ListNode(3, ListNode(5, None))))
}   
test2 = {
    'head': ListNode(1, ListNode(2,None)), 
    'n': 1,
    'output_exp': ListNode(1, None)
}  
tests = [test1]
for test in tests:
    res = SolutionA().removeNthFromEnd(test['head'], test['n'])
    print('head: {}, n: {}\nResultado esperado: {}\nResultado: {}'\
          .format(test['head'], test['n'], test['output_exp'], res))