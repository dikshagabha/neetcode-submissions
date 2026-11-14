class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        #lights.sort()
        nodes = defaultdict(int)
        for src, dest in lights:
            nodes[src-dest]+= 1
            nodes[src+dest+1] -=1

        
        cur, max_val = 0, 0
        res = 0
        for src in sorted(nodes):
            cur+=nodes[src]
            if cur>max_val:
                max_val=cur
                res = src
        return res
        maxm = 0
        for i, j in m:
            maxm = max(maxm, j)
        
        for i, j in m:
            if j==maxm:
                return i
        return m[-1][0]
