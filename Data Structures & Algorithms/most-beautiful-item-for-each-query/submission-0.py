class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        sitems = sorted(items, key=lambda x: x[1])
        curres = {}
        j = len(sitems)-1
        q = sorted(queries)
        
        for i in range(len(q)-1, -1, -1):
            maxb = q[i]
            while j>0 and maxb<sitems[j][0]:
                j-=1
            if j==0 and maxb<sitems[j][0]:
                curres[maxb] = 0
            else:
                curres[maxb] = sitems[j][1]
        
        res = []
        for i  in queries:
            res.append(curres[i])
        return res
