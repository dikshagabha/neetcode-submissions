class Solution:
    def scoreOfString(self, s: str) -> int:
        res=0
        for r in range(1, len(s)):
            res+=abs(ord(s[r-1]) - ord(s[r]))
            
        return res