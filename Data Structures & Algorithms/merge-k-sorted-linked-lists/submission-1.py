# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        while True:
            found = False
            leastVal = float('inf')
            leastIndex = -1
            for i in range(len(lists)):
                if (lists[i] is not None):
                    found = True
                    if (lists[i].val<leastVal):
                        leastIndex = i
                        leastVal = lists[i].val

            if found == False:
                break

            else:
                nodes.append(lists[leastIndex])
                lists[leastIndex] = lists[leastIndex].next
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        if (len(nodes)==0):
            return None
        return nodes[0]