class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if (grid[i][j]==0):
                    q = deque()
                    q.append((i,j,0))
                    while (len(q)>0):
                        a,b,dist = q.popleft()
                        if (a==i and b==j) or (a<m and a>=0 and b<n and b>=0 and grid[a][b]>0 and dist<grid[a][b]):
                            grid[a][b] = min(grid[a][b],dist)
                            q.append((a,b+1,dist+1))
                            q.append((a,b-1,dist+1))
                            q.append((a+1,b,dist+1))
                            q.append((a-1,b,dist+1))