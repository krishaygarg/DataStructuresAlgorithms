# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        n = 0
        curr = head
        while (curr is not None):
            n+=1
            curr = curr.next
        if (n<=2):
            return
        start = head
        for i in range((n-1)//2):
            start = start.next
        temp = start.next
        start.next = None
        start = temp
        # reverse
        curr = start
        currNext = curr.next
        curr.next = None
        while currNext is not None:
            nextNode = currNext.next
            currNext.next = curr
            curr = currNext
            currNext = nextNode
        start = head
        end = curr
        for i in range(n-1):
            if start == end:
                break
            print(start.val,end.val)
            if (i%2==0):
                next = start.next
                start.next = end
                start = next
            else:
                next = end.next
                end.next = start
                end = next

            
                  
        
            
