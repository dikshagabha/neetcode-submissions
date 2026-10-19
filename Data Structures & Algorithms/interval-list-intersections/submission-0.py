class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        m = {}
        def set_map(l):
            for s, e in l:
                m[s] = m.get(s, 0)+1
                m[e+1] = m.get(e+1, 0)-1

        set_map(firstList)
        set_map(secondList)
        res = []
        active = 0
        for i in sorted(m):
            if active==2:
                res.append([prev, i-1])
            active+=m[i]
            prev= i
        return res