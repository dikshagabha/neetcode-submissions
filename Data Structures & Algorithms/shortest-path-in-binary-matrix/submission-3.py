class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        q = [(0, 0, 1)]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0),
                  (1, 1), (-1, -1), (1, -1), (-1, 1)]
        n = len(grid)
        visited = set((0, 0))
        while q:
            x, y, l = q.pop(0)
            if (x,y) == (n-1, n-1):
                return l
            for dx, dy in directions:
                xnew = x+dx
                ynew = y+dy
                if (0<=xnew <n and 0<=ynew<n and grid[xnew][ynew]==0 and (xnew, ynew) not in visited):
                    visited.add((xnew, ynew))
                    q.append(((xnew, ynew, l+1)))

            
        return -1
