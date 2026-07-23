class Solution:
    def isPathCrossing(self, path: str) -> bool:
        m = {'N':(1, 0), 'S': (-1, 0), 'E':(0, 1), 'W':(0,-1)}
        cur = (0, 0)
        visited =set()
        visited.add(cur)
        for i in path:
            next_p = (cur[0]+m[i][0], cur[1]+m[i][1])
            if next_p in visited:
                return True
            
            visited.add(cur)
            cur = next_p
        return False