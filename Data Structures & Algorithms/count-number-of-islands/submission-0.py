class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0]*n for _ in range(m)]
        count = 0
        stack = []
        for i in range(m):
            for j in range(n):
                if (grid[i][j] == "1"):
                    if (visited[i][j]==0):
                        visited[i][j]=1
                        count+=1
                        stack.append((i,j))
                    while (len(stack)>0):
                        a,b = stack.pop()
                        print(i,j,a,b)
                        if (a<m-1 and visited[a+1][b]==0 and grid[a+1][b]=="1"):
                            visited[a+1][b] = 1
                            stack.append((a+1,b))
                        if (a>0 and visited[a-1][b]==0 and grid[a-1][b]=="1"):
                            visited[a-1][b] = 1
                            stack.append((a-1,b))
                        if (b<n-1 and visited[a][b+1]==0 and grid[a][b+1]=="1"):
                            visited[a][b+1] = 1
                            stack.append((a,b+1))
                        if (b>0 and visited[a][b-1]==0 and grid[a][b-1]=="1"):
                            visited[a][b-1] = 1
                            stack.append((a,b-1))
        return count
                        
                    
