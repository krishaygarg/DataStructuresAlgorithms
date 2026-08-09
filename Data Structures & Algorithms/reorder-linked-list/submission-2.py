# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        original = []
        curr = head
        while curr is not None:
            original.append(curr)
            curr = curr.next
        # reordered = []
        n = len(original)
        i, j = 0, n-1
        for a in range(n):
            if i==j:
                original[i].next = None
            elif (a%2==0):
                original[i].next = original[j]
                i+=1
            else:
                original[j].next = original[i]
                j-=1
        
            

        # n = 0
        # curr = head
        # while (curr is not None):
        #     n+=1
        #     curr = curr.next
        # if (n<=2):
        #     return
        # start = head
        # for i in range((n-1)//2):
        #     start = start.next
        # temp = start.next
        # start.next = None
        # start = temp
        # # reverse
        # curr = start
        # currNext = curr.next
        # curr.next = None
        # while currNext is not None:
        #     nextNode = currNext.next
        #     currNext.next = curr
        #     curr = currNext
        #     currNext = nextNode
        # start = head
        # end = curr
        # for i in range(n-1):
        #     if start == end:
        #         break
        #     print(start.val,end.val)
        #     if (i%2==0):
        #         next = start.next
        #         start.next = end
        #         start = next
        #     else:
        #         next = end.next
        #         end.next = start
        #         end = next

            
                  
        
            
