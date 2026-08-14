class Solution:
    def solve(self, board: List[List[str]]) -> None:
        stack = []
        for i in range(len(board)):
            if (board[i][0]=='O'):
                stack.append((i,0))
            if (board[i][-1]=='O'):
                stack.append((i,len(board[0])-1))
        for i in range(len(board[0])):
            if (board[0][i]=='O'):
                stack.append((0,i))
            if (board[-1][i]=='O'):
                stack.append((len(board)-1,i))
        while (len(stack)>0):
            current = stack.pop()
            # print(current)

            if (current[0]<0 or current[0]>=len(board) or current[1]<0 or current[1]>=len(board[0]) or board[current[0]][current[1]]!='O'):
                continue

            board[current[0]][current[1]]='1'
            stack.append((current[0]-1,current[1]))
            stack.append((current[0]+1,current[1]))
            stack.append((current[0],current[1]-1))
            stack.append((current[0],current[1]+1))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j]=='O'):
                    board[i][j]='X'
                elif board[i][j]=='1':
                    board[i][j]='O'
        # return board

            