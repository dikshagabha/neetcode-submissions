class Solution:
    def partitionString(self, s: str) -> int:
        
        cchars = set()
        res = 1
        for r in range(len(s)):
            if s[r] in cchars:
                res+=1
                cchars.clear()
            cchars.add(s[r])
        return res