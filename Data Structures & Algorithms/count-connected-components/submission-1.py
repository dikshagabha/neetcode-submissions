class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        p = [i for i in range(n)]
        r = [1]*n
        def get_root(e):
            e = p[e]
            while p[e] != e:
                e = p[e]
            return p[e]
        
        def set_p(e1, e2):
            r1, r2 = get_root(e1), get_root(e2)

            if r1 == r2:
                return 0
            if r[r1]>r[r2]:
                p[r1] = r2
                r[r1]+=r[r2]
            else:
                p[r2] = r1
                r[r2]+=r[r1]
            return -1
        
        res = n
        for e1, e2 in edges:
            c = set_p(e1, e2)
            
            res+=c
        
        return res
