class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        #lights.sort()
        nodes = []
       
        cur = {}
        for src, dest in lights:
            nodes.append((src-dest, 1))
            nodes.append((src+dest+1, -1))

        nodes.sort()
        d = 0
        m = [(-float('inf'), 0)]
        heapq.heapify(m)
        for src, val in nodes:
            s, prev  = m[-1]
           
            heapq.heappush(m, (src, prev+val))
        
        maxm = 0
        for i, j in m:
            maxm = max(maxm, j)
        
        for i, j in m:
            if j==maxm:
                return i
        return m[-1][0]
