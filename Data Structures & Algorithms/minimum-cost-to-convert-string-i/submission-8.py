
class Solution:
    def minimumCost(self, source: str, target: str,
                    original: List[str], changed: List[str],
                    cost: List[int]) -> int:

        dis = [[float('inf')] * 26 for _ in range(26)]

        for i in range(26):
            dis[i][i] = 0

        for s, d, c in zip(original, changed, cost):
            u = ord(s) - ord('a')
            v = ord(d) - ord('a')
            dis[u][v] = min(dis[u][v], c)

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dis[i][j] = min(
                        dis[i][j],
                        dis[i][k] + dis[k][j]
                    )

        res = 0

        for s, t in zip(source, target):
            u = ord(s) - ord('a')
            v = ord(t) - ord('a')

            if dis[u][v] == float('inf'):
                return -1

            res += dis[u][v]

        return res
