class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        sides = [(0,1), (1,0), (0,-1),(-1,0)]
        s = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==0:
                    continue
                c = 4
                for difx, dify in sides:
                    if i+difx in range(len(grid)) and j+dify in range(len(grid[i])) and grid[i+difx][j+dify]!=0:
                        c-=1
                s += c
        return s
