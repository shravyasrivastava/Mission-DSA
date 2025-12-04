class Solution(object):
    def solve(self, board):
        if not board or not board[0]:
            return
        rows,cols=len(board),len(board[0])
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or board[r][c]!='O':
                return
            board[r][c]='S'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for i in range(rows):
            if board[i][0]=='O':
                dfs(i,0)
            if board[i][cols-1]=='O':
                dfs(i,cols-1)
        for j in range(cols):
            if board[0][j]=='O':
                dfs(0,j)
            if board[rows-1][j]=='O':
                dfs(rows-1,j)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='O':
                    board[r][c]='X'
                elif board[r][c]=='S':
                    board[r][c]='O'
        