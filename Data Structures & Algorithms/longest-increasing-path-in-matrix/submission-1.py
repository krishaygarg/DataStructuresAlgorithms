from collections import deque
class Solution:
    def helper(self,i,j,dist,previous):
        if (0<=i<len(self.matrix) and 0<=j<len(self.matrix[0])):
            if (self.matrix[i][j]>previous):
                self.degrees[i][j]-=1
                if (self.degrees[i][j]==0):
                    self.queue.append([(i,j),dist+1])
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        self.degrees = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        self.queue = deque() # [(i,j),0]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i>0 and matrix[i][j]>matrix[i-1][j]:
                    self.degrees[i][j]+=1
                if j>0 and matrix[i][j]>matrix[i][j-1]:
                    self.degrees[i][j]+=1
                if i<len(matrix)-1 and matrix[i][j]>matrix[i+1][j]:
                    self.degrees[i][j]+=1
                if j<len(matrix[0])-1 and matrix[i][j]>matrix[i][j+1]:
                    self.degrees[i][j]+=1 
                if (self.degrees[i][j]==0):
                    self.queue.append([(i,j),1])
        print(self.degrees)
        maxDist = 0
        while (len(self.queue)>0):
            point, distance = self.queue.popleft()
            i, j = point
            print(i,j,distance)
            maxDist = max(maxDist, distance)
            self.helper(i+1,j,distance,matrix[i][j])
            self.helper(i-1,j,distance,matrix[i][j])
            self.helper(i,j+1,distance,matrix[i][j])
            self.helper(i,j-1,distance,matrix[i][j])
        return maxDist
