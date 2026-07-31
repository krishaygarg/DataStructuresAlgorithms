class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        print(adj)
        visited = [0]*n
        count = 0
        for i in range(len(visited)):
            if (not visited[i]):
                print(i, visited)
                count+=1
                q = deque()
                q.append(i)
                while (len(q)>0):
                    cur = q.popleft()
                    visited[cur] = 1
                    for j in adj[cur]:
                        if (not visited[j]):
                            q.append(j)
                            visited[j]=1
        return count

