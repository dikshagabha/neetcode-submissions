class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m<2 and m<2:
            return 1
        pathmap = [0]
        for i in range(1, n):
            pathmap.append(1)

        for i in range(m-1):
            curmap = [1]
            for j in range(1, n):
                curmap.append(curmap[-1]+pathmap[j])
            pathmap=curmap

        return pathmap[-1]