class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols = len(grid),len(grid[0])
        q = deque()
        visit = set()
        directions = [[-1,0],[1,0],[0,1],[0,-1]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist

                for dr,dc in directions:
                    nr,nc = r + dr,c + dc

                    if (nr < 0 or nr == rows or 
                        nc < 0 or nc == cols or grid[nr][nc]== -1 or 
                        (nr,nc)in visit):
                        continue
                    q.append((nr,nc))
                    visit.add((nr,nc))
            dist += 1 #distance incremented after the entire leevel is processed
                        