class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        vals = {}

        for i in range(len(s)-9):
            vals[s[i:i+10]] = vals.get(s[i:i+10], 0)+1

        res = []

        for st, val in vals.items():
            if val>=2:
                res.append(st)
        return res