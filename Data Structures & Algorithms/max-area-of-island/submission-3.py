class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        path = []
        visited = set()
        neighbours = [(0,1),(1,0),(-1,0), (0,-1)]
        n = len(grid)
        m = len(grid[0])
        def define_path(i, j):
            nonlocal path
            if (i, j) in visited:
                return 0
            #path.append((i, j))
            visited.add((i ,j))
            res = 1
            for dx , dy in neighbours:
                r, c = i+dx, j+dy
                if r>=0 and r<n and c>=0 and c<m and grid[r][c]==1:
                    res+=define_path(r, c)
            return res
        res = 0
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and grid[i][j] !=0 :
                    res = max(res, define_path(i, j))
                  
        
        return res
