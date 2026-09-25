class Solution:
    def recurse(self, matrix, i, j):
        # if (0<=i<len(matrix) and 0<=i<len(matrix[0])):
        if (i,j) in self.dp:
            return self.dp[(i,j)]
        longest = 1
        if (i>0 and matrix[i-1][j]<matrix[i][j]):
            longest = max(longest,1+self.recurse(matrix,i-1,j))
        if (j>0 and matrix[i][j-1]<matrix[i][j]):
            longest = max(longest,1+self.recurse(matrix,i,j-1))
        if (i<len(matrix)-1 and matrix[i+1][j]<matrix[i][j]):
            longest = max(longest,1+self.recurse(matrix,i+1,j))
        if (j<len(matrix[0])-1 and matrix[i][j+1]<matrix[i][j]):
            longest = max(longest,1+self.recurse(matrix,i,j+1))
        self.dp[(i,j)]=longest
        print(i,j,longest)
        return longest
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.dp = dict()
        best = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                best = max(best,self.recurse(matrix,i,j))
        return best
