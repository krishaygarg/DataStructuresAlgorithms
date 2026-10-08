import copy
class Solution:
    def dfs(self,i,j):
        if (i<0 or i>=len(self.canVisit) or j<0 or j>=len(self.canVisit[0])):
            return
        if (self.grid[i][j]==0 or self.canVisit[i][j]==1):
            return
        self.canVisit[i][j] = 1
        self.dfs(i+1,j)
        self.dfs(i-1,j)
        self.dfs(i,j+1)
        self.dfs(i,j-1)
    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.canVisit = [[0]*len(grid[0]) for _ in range(len(grid))]
        self.grid = grid
        print(self.canVisit)
        total = 0
        for i in range(len(grid[0])):
            self.dfs(0,i)
            self.dfs(len(grid)-1,i)
        for i in range(len(grid)):
            self.dfs(i,0)
            self.dfs(i,len(grid[0])-1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j]==1 and self.canVisit[i][j]==0):
                    total+=1
        return total
