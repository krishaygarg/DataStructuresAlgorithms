"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = dict()
        if head is None:
            return None
        curr = head
        while (curr is not None):
            # print(map)
            # print(curr.val, curr.next, curr.random)
            if curr not in map:
                map[curr] = Node(curr.val,None,None)
            if curr.next is not None:
                if curr.next not in map:
                    map[curr.next] = Node(curr.next.val,None,None)
                map[curr].next = map[curr.next]
            if curr.random is not None:
                if curr.random not in map:
                    map[curr.random] = Node(curr.random.val,None,None)
                map[curr].random = map[curr.random]
            curr = curr.next
    
        return map[head]