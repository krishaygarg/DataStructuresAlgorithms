class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(i,j):
            if (i>=m or j>=n or i<0 or j<0 or visited[i][j]==1 or grid[i][j]==0):
                return 0
            count = 1
            visited[i][j]=1
            count+=(dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1))
            return count



        best = 0
        visited = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if (grid[i][j]==1 and visited[i][j]==0):
                    best = max(best,dfs(i,j))
        return best