from collections import deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # find some leaf node
        # run a topological sort till we are only left with cycle
        # check which edge is last
        n = len(edges)
        adj = [[] for _ in range(n)]
        degrees = [0]*n
        for edge in edges:
            adj[edge[0]-1].append(edge[1]-1)
            adj[edge[1]-1].append(edge[0]-1)
            degrees[edge[0]-1]+=1
            degrees[edge[1]-1]+=1
        queue = deque()
        for i in range(n):
            if (degrees[i]==1):
                queue.append(i)

                
        if len(queue)==0:
            return edges[-1]
        safe = set()
        while (len(queue)>0):
            current = queue.popleft()
            safe.add(current)
            print(current)
            for next_node in adj[current]:
                degrees[next_node]-=1
                if (degrees[next_node]==1):
                    queue.append(next_node)
        for i in range(n-1, -1, -1):
            if (edges[i][0]-1 not in safe and edges[i][1]-1 not in safe):
                return edges[i]        

        