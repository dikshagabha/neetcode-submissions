class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        m = {}
        p = []
        for i, j in trust:
           m[j] = m.get(j,0)+1
           p.append(i)
        
        for judge, val in m.items():
            if val == n-1 and judge not in p:
                return judge
        return -1
                