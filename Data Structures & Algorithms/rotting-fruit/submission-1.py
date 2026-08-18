class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        q = []
        req = 0
        v = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                    v.add((i, j))
                    req += 1
                elif grid[i][j] == 1:
                    req += 1

        q = [q]
        l = 0

        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            cur = q.pop()
            level = []

            for r, c in cur:
                for dr, dc in d:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < n and 0 <= nc < m):
                        continue

                    if grid[nr][nc] == 1 and (nr, nc) not in v:
                        v.add((nr, nc))
                        level.append((nr, nc))

            if level:
                l += 1
                q.append(level)

        return l if len(v) == req else -1