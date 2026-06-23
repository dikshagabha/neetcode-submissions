class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = []
        directions = [(0,1), (1,0), (-1,0),(0,-1)]
        def get_valid_neigh(i, j):
            if (i, j) not in visited:
                visited.append((i, j))
            
            for dx, dy in directions:
                xnew, ynew = dx+i, dy+j
                if xnew>=0 and ynew>=0 and xnew< len(grid) and ynew<len(grid[xnew]) and grid[xnew][ynew] == '1' and (xnew, ynew) not in visited:
                    get_valid_neigh(xnew, ynew)

            return
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    get_valid_neigh(i, j)
                    res+=1
        return res




