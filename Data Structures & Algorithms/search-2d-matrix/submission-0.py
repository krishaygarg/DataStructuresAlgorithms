class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix)*len(matrix[0])-1
        while (start<=end):
            middle = (start+end)//2
            row = middle // len(matrix[0])
            col = middle % len(matrix[0])
            print(middle)
            print(row,col)
            if (matrix[row][col]>target):
                end = middle-1
            elif (matrix[row][col]==target):
                return True
            else:
                start = middle+1
        return False