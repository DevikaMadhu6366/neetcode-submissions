class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols = len(board),len(board[0])
        
        #capture unsurrounded or 0 regions
        def capture(r,c):
            if (r < 0 or r == rows or
                c < 0 or c == cols or 
                board[r][c] != "O"):
                return
            board[r][c] = "T" # [mark 0 as T]
            capture(r+ 1,c)
            capture(r - 1,c)
            capture(r,c + 1)
            capture(r, c- 1)

        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O" and
                    (r in [0,rows - 1] or c in [0,cols - 1])):
                    capture(r,c)


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":#capture surrounded regions(0-X)
                    board[r][c] = "X"
                elif board[r][c] == "T":#uncapture unsurrounded regions(T-0)
                    board[r][c] = "O"

                




