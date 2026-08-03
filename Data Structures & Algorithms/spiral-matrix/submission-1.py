class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        visited = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        ans = []
        dir = 1
        i, j = 0, 0
        changed = True
        count = 0
        
        while (len(ans)<m*n):
            count+=1
            print(i,j,dir)
            if changed:
                ans.append(matrix[i][j])
            visited[i][j] = 1
            changed = False
            if dir == 0:
                if (i==m-1 or visited[i+1][j]==1):
                    dir = 3
                    continue
                else:
                    i+=1
                    changed = True
            if dir == 1:
                if (j==n-1 or visited[i][j+1]==1):
                    dir = 0
                    continue
                else:
                    j+=1
                    changed = True
            if dir == 2:
                if (i==0 or visited[i-1][j]==1):
                    dir = 1
                    continue
                else:
                    i-=1
                    changed = True
            if dir == 3:
                if (j==0 or visited[i][j-1]==1):
                    dir = 2
                    continue
                else:
                    j-=1
                    changed = True
        return ans