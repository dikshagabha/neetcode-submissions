class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        q = [(0, 0, 0)]
        d = [(0, 1),(1, 0), (-1,0),(0,-1)]
        n = len(heights)
        m = len(heights[0])
        visited = set()
        res = 0
        while len(q):
            h,r,c = heapq.heappop(q)
            if (r,c) in visited:
                continue
            visited.add((r, c))
            if (r, c) == (n-1, m-1):
                return h
            
            for dr, dc in d:
                rn, cn = dr+r, c+dc  
                if rn in range(n) and cn in range(m) and (rn,cn) not in visited:
                    diff = max(h, abs(heights[r][c]-heights[rn][cn]))
                    heapq.heappush(q, (diff, rn,cn))
                  
        return res