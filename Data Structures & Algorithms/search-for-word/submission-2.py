class Solution:
    def backtrack(self,i,j,pos):
        print(i,j,pos)
        if pos == len(self.word):
            return True
        if i<0 or i>=len(self.board) or j<0 or j>=len(self.board[0]):
            return False
        if (self.board[i][j]!=self.word[pos] or self.used[i][j]):
            return False
        self.used[i][j] = True
        found = self.backtrack(i-1,j,pos+1) or self.backtrack(i+1,j,pos+1) or self.backtrack(i,j-1,pos+1) or self.backtrack(i,j+1,pos+1)
        self.used[i][j] = False
        return found
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        self.board = board
        self.used = [[False]*n for _ in range(m)]
        self.word = word
        for i in range(m):
            for j in range(n):
                if self.backtrack(i,j,0):
                    return True
        return False
