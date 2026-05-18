class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        def find_neighbours(i, j):
            if i not in range(len(grid)) or j not in range(len(grid[0])) or grid[i][j]!=1 or (i, j) in visited:
                return 0

            visited.add((i, j))
           
            return 1+ find_neighbours(i+1, j) + find_neighbours(i, j+1) +find_neighbours(i-1, j)+find_neighbours(i, j-1)

        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1 and (i, j) not in visited:
                    area = find_neighbours(i, j)
                    island = max(island, area)
        
        return island