class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        vals = {}
        res = []
        for i in range(len(s)-9):
            st =s[i:i+10]
            vals[st] = vals.get(st, 0)+1
            if vals[st]==2:
                res.append(st)


        
        # for st, val in vals.items():
        #     if val>=2:
        #         res.append(st)
        return res