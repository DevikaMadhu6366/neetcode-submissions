class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows ,cols = len(board),len(board[0]) # no of rows and cols
        path = set() #store cells currently using in current route

        def dfs(r,c,i):#row and col of current path and which char of word we are currently trying to match
            if i == len(word):
                return True

            if(r<0 or c<0 or #(0,-1) out of board
                r>=rows or c>=cols or
                word[i]!=board[r][c] or
                (r,c) in path): #ABA 
                return False

            path.add((r,c))
            res = (dfs(r+1,c,i+1)or
                    dfs(r-1,c,i+1)or
                    dfs(r,c+1,i+1)or
                    dfs(r,c-1,i+1))

            path.remove((r,c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                   return True
        return False



