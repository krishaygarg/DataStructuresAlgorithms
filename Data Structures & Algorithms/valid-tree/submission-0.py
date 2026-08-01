class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        visited = [False]*n
        q = [0]
        count = 0
        while (len(q)>0):
            count+=1
            element = q.pop()
            visited[element] = True
            for i in adj[element]:
                if (not visited[i]):
                    q.append(i)

        return bool(count==n)