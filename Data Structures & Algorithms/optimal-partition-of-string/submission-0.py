class Solution:
    def partitionString(self, s: str) -> int:
        
        cchars = {}
        l = 0
        cchars[s[l]] = 1
        res = 1
        for r in range(1, len(s)):
            cchars[s[r]] = cchars.get(s[r], 0)+1
            if cchars[s[r]] == 2:
                cchars = {}
                l = r
                cchars[s[l]] = 1
                res+=1
        return res