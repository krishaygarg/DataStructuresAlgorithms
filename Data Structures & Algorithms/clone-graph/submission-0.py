"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        map = dict()
        if node is None:
            return None
        stack = [node]
        visited = set()
        while (len(stack)>0):
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                if current not in map:
                    map[current] = Node(current.val,[])
                for next in current.neighbors:
                    if next not in map:
                        map[next] = Node(next.val,[])
                    map[current].neighbors.append(map[next])
                    stack.append(next)
        return map[node]