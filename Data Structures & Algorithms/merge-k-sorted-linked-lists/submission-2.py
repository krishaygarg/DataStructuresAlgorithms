# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        vals = []
        for i in range(len(lists)):
            if (lists[i] is not None):
                heapq.heappush(vals,[lists[i].val,i])
        while len(vals)>0:
            
                leastVal, leastIndex = heapq.heappop(vals)
                nodes.append(lists[leastIndex])
                lists[leastIndex] = lists[leastIndex].next
                if (lists[leastIndex] is not None):
                    heapq.heappush(vals,[lists[leastIndex].val,leastIndex])
                
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        if (len(nodes)==0):
            return None
        return nodes[0]