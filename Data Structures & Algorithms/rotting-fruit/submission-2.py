class Solution:
    def bfs(self,fresh,q,m,n,grid):                
            while (len(q)>0):
                i,j,dist = q.popleft()
                print(i,j,dist)
                if i<0 or i>=m or j<0 or j>=n:
                    continue
                if grid[i][j]==1:
                    grid[i][j]=2
                    fresh-=1
                    if (fresh==0):
                        return dist
                    q.append((i+1,j,dist+1))
                    q.append((i-1,j,dist+1))
                    q.append((i,j-1,dist+1))
                    q.append((i,j+1,dist+1))
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh = 0
        q = deque()
        m, n = len(grid), len(grid[0])


        for i in range(m):
            for j in range(n):
                if (grid[i][j]==1):
                    fresh+=1
                elif grid[i][j]==2:
                    fresh+=1
                    grid[i][j]=1
                    q.append((i,j,0))
        if fresh==0:
            return 0
        ans = self.bfs(fresh,q,m,n,grid)
        if ans is None:
            return -1
        return ans
            