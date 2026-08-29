# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        prev = None
        cur = head
        
        while (l1 is not None or l2 is not None):
            next = ListNode()
            a, b = 0, 0
            if l1 is not None:
                a = l1.val
            if l2 is not None:
                b = l2.val
            cur.val+=a+b
            next.val += cur.val//10
            cur.val%=10
            cur.next = next
            prev = cur
            cur = next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if (cur.val==0):
            prev.next = None
        return head