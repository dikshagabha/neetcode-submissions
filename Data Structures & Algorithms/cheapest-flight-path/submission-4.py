import copy
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        neigh = {}
        paths = []
        visited = [src]
        maxp = float('inf')
        for s, d, p in flights:
            if s not in neigh:
                neigh[s] = []
            neigh[s].append([d, p])
        def path(i, p):
            nonlocal maxp
            if i==dst:
                curpath = copy.deepcopy(visited)
                maxp = min(p, maxp)
                return 
            if i not in neigh:
                return
            for j, price in neigh[i]:
                
                if (p+price)>maxp:
                    continue
                visited.append(j)
                if len(visited)>k+2:
                    visited.pop()
                    continue
                path(j, p+price)
                visited.pop()
        
        path(src, 0)
        if maxp== float('inf'):
            return -1
        return maxp